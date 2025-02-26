from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Agent
from .serializers import AgentSerializer

class AgentListCreateView(generics.ListCreateAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

class AgentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializer
