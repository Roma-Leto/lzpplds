"""
This will route the WebSocket connections to the consumers.
"""

from django.urls import path
from chat.consumers import ChatConsumer


websocket_urlpatterns = [
    # path("", ChatConsumer.as_asgi()),
    path('<int:recipient_id>/', ChatConsumer.as_asgi()),
]
