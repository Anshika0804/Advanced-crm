import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from channels.db import database_sync_to_async 
from .models import Notification
from .serializers import NotificationSerializer

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            self.user = self.scope["user"]
            self.group_name = f"user_{self.user.id}"
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()


    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_notification(self, event):
        message = event['message']
        print(f"Sending WS message to user {self.user.id}: {message}")  # Debug line
        await self.send(text_data=json.dumps(message))

    # @database_sync_to_async
    # def create_notification(self, lead, message):
    #     return Notification.objects.create(user=self.user, lead=lead, message=message)

    
