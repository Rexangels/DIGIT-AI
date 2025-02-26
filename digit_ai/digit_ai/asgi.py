"""
ASGI config for digit_ai project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""
# digit_ai/asgi.py
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digit_ai.settings')

application = get_asgi_application()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import communication.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'digit_ai.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            communication.routing.websocket_urlpatterns
        )
    ),
})
