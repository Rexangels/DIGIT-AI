# communication/services.py
import json
import uuid
from datetime import datetime

class MessageProtocol:
    @staticmethod
    def create_message(sender_id, recipient_id, message_type, content, metadata=None):
        """
        Create a standardized message for agent communication
        
        Parameters:
        - sender_id: ID of the sending agent
        - recipient_id: ID of the recipient agent (or 'broadcast' for all)
        - message_type: Type of message (task, response, status, etc.)
        - content: Main message content
        - metadata: Additional information
        
        Returns:
        - Formatted message dictionary
        """
        if metadata is None:
            metadata = {}
            
        return {
            'message_id': str(uuid.uuid4()),
            'timestamp': datetime.utcnow().isoformat(),
            'sender_id': sender_id,
            'recipient_id': recipient_id,
            'message_type': message_type,
            'content': content,
            'metadata': metadata
        }
    
    @staticmethod
    def create_task_message(sender_id, recipient_id, task_description, priority='medium', deadline=None):
        """Helper method to create a task assignment message"""
        metadata = {
            'priority': priority,
            'deadline': deadline,
            'status': 'assigned'
        }
        
        return MessageProtocol.create_message(
            sender_id, 
            recipient_id, 
            'task_assignment',
            task_description,
            metadata
        )
    
    @staticmethod
    def create_response_message(sender_id, recipient_id, original_message_id, content, status='completed'):
        """Helper method to create a response message"""
        metadata = {
            'original_message_id': original_message_id,
            'status': status
        }
        
        return MessageProtocol.create_message(
            sender_id,
            recipient_id,
            'task_response',
            content,
            metadata
        )