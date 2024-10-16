from channels.generic.websocket import AsyncWebsocketConsumer
import json

class UserConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.channel_layer.group_add("user_notifications", self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("user_notifications", self.channel_name)

    async def notify_user_creation(self, event):
        message = event['message']
        await self.send(text_data=json.dumps({
            'message': message
        }))
