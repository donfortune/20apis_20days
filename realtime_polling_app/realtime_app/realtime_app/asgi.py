import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack  # Import the authentication middleware
from app_web import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realtime_app.settings")



application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(  # Use AuthMiddlewareStack for WebSocket
        URLRouter(
            routing.websocket_urlpatterns
        )
    ),
})

# ASGI_APPLICATION = 'realtime_app.asgi.application'
