# communication/routing.py
from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/project/(?P<project_id>\w+)/$', consumers.AgentCommunicationConsumer.as_asgi()),
]
