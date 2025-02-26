import json
import logging
import openai
from .models import Agent, AgentType
from communication.services import MessageProtocol
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

logger = logging.getLogger(__name__)

class AgentService:
    @staticmethod
    def create_main_agent(project, model_type='gpt4'):
        try:
            agent_type, _ = AgentType.objects.get_or_create(
                name="Main Agent",
                defaults={
                    'description': "Coordinates other agents and manages tasks",
                    'capabilities': {'coordination': True, 'planning': True}
                }
            )
            return Agent.objects.create(
                name=f"{project.name} Main Agent",
                agent_type=agent_type,
                project=project,
                status='idle',
                model_type=model_type,
                is_main_agent=True
            )
        except Exception as e:
            logger.error(f"Error creating main agent: {e}")
            raise

    @staticmethod
    def process_message(message):
        try:
            if message['message_type'] == 'task_assignment':
                recipient = Agent.objects.get(id=message['recipient_id'])
                recipient.status = 'working'
                recipient.current_task = message['content']
                recipient.save()
                
                # Call LLM API (with error handling)
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-4" if recipient.model_type == 'gpt4' else "gpt-3.5-turbo",
                        messages=[
                            {"role": "system", "content": f"You are a {recipient.agent_type.name} specialized in {recipient.agent_type.capabilities}."},
                            {"role": "user", "content": message['content']}
                        ]
                    )
                    response_text = response.choices[0].message.content
                except Exception as api_error:
                    logger.error(f"LLM API error: {api_error}")
                    response_text = "Error processing your request."

                return MessageProtocol.create_response_message(
                    sender_id=message['recipient_id'],
                    recipient_id=message['sender_id'],
                    original_message_id=message['message_id'],
                    content=response_text
                )
        except Agent.DoesNotExist:
            logger.error("Recipient agent not found.")
            return MessageProtocol.create_response_message(
                sender_id=message['recipient_id'],
                recipient_id=message['sender_id'],
                original_message_id=message['message_id'],
                content="Recipient agent not found."
            )
        except Exception as e:
            logger.error(f"Unexpected error in process_message: {e}")
            return None

    @staticmethod
    def send_message(message, project_id):
        try:
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'project_{project_id}',
                {
                    'type': 'agent_message',
                    'message': message['content'],
                    'sender': message['sender_id']
                }
            )
        except Exception as e:
            logger.error(f"Error sending message: {e}")
