from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from app1.consumers import YourConsumer

application = ProtocolTypeRouter(
    {
        'websocket': URLRouter([
            path('your-url/', YourConsumer.as_asgi()),
        ]),
    }
)