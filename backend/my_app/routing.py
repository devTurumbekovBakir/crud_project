from django.urls import path

from my_app.consumers import UserConsumer

websocket_urlpatterns = [
    path('ws/users/', UserConsumer.as_asgi()),
]
