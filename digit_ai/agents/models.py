# agents/models.py
from django.db import models
from django.conf import settings

class AgentType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    capabilities = models.JSONField()
    
    def __str__(self):
        return self.name

class Agent(models.Model):
    STATUS_CHOICES = [
        ('idle', 'Idle'),
        ('working', 'Working'),
        ('coopa', 'CO-OPA Mode'),
        ('error', 'Error'),
        ('completed', 'Task Completed'),
    ]
    
    MODEL_CHOICES = [
        ('gpt4', 'GPT-4 Turbo'),
        ('claude', 'Claude'),
        ('mistral', 'Mistral'),
        ('llama', 'Llama'),
    ]
    
    name = models.CharField(max_length=100)
    agent_type = models.ForeignKey(AgentType, on_delete=models.CASCADE)
    project = models.ForeignKey('projects.Project', on_delete=models.CASCADE)
    created_by = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL, related_name='created_agents')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='idle')
    current_task = models.TextField(null=True, blank=True)
    model_type = models.CharField(max_length=50, choices=MODEL_CHOICES, default='gpt4')
    is_main_agent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    last_active = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} ({self.agent_type.name})"






