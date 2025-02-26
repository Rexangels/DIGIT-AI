import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)

class AgentCommunicationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.project_id = self.scope['url_route']['kwargs']['project_id']
        self.room_group_name = f'project_{self.project_id}'
        try:
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
            logger.info(f"WebSocket connected: {self.channel_name} in {self.room_group_name}")
        except Exception as e:
            logger.error(f"WebSocket connection error: {e}")
            await self.close()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        logger.info(f"WebSocket disconnected: {self.channel_name}")

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
            message = data.get('message')
            sender = data.get('sender')
            # Broadcast the message to the group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'agent_message',
                    'message': message,
                    'sender': sender
                }
            )
        except Exception as e:
            logger.error(f"Error receiving message: {e}")

    async def agent_message(self, event):
        message = event.get('message')
        sender = event.get('sender')
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))
