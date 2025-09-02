import json
from channels.generic.websocket import AsyncWebsocketConsumer


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # If you use AuthMiddlewareStack, user is automatically added to scope
        if self.scope["user"].is_anonymous:
            await self.close()
        else:
            self.user = self.scope["user"]
            self.group_name = f"user_{self.user.id}"

            # Add this connection to the user-specific group
            await self.channel_layer.group_add(self.group_name, self.channel_name)
            await self.accept()

    async def disconnect(self, close_code):
        # Remove from group on disconnect
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def send_notification(self, event):
        # Handler when a notification is sent via group_send
        message = event['message']
        print(f"Sending WS message to user {self.user.id}: {message}")
        await self.send(text_data=json.dumps(message))
