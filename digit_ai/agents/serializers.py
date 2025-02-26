from rest_framework import serializers
from .models import Agent, AgentType

class AgentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgentType
        fields = '__all__'

class AgentSerializer(serializers.ModelSerializer):
    agent_type = AgentTypeSerializer(read_only=True)
    
    class Meta:
        model = Agent
        fields = '__all__'
#
#