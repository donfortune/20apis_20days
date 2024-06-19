import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from app_web import routing

django_asgi_app = get_asgi_application()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "realtime_app.settings")
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthenticationMiddlewareStack(
        URLRouter(
            routing.websocket_urlpatterns
        )
    )
    # Just HTTP for now. (We can add other protocols later.)
})

ASGI_APPLICATION = 'realtime_app.asgi.application'




