from django.urls import re_path
from .consumers import AsyncWebsocketConsumer

websocket_urlpatterns = [
    re_path(r'ws/users/$', AsyncWebsocketConsumer.as_asgi()),
]