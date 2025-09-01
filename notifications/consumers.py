import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from channels.db import database_sync_to_async 
from urllib.parse import parse_qs
from django.contrib.auth.models import AnonymousUser
# from django.conf import crm_project.authentication import get_user_from_token  

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        #TOKEN VALIDATION
        # query_string = self.scope["query_string"].decode()  # bytes -> string
        # params = parse_qs(query_string)
        # token_list = params.get("token", [])

        # if not token_list:
        #     await self.close(code=4001)  # token missing
        #     return

        # token = token_list[0]

        # # Validate token and get user
        # self.user = await get_user_from_token(token)
        # if self.user is None or isinstance(self.user, AnonymousUser):
        #     await self.close(code=4001)  # invalid token
        #     return


        # AuthMiddlewareStack automatically associates scope["user"] based on Django’s session cookies.
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
        print(f"Sending WS message to user {self.user.id}: {message}")  
        await self.send(text_data=json.dumps(message))
        # handler method invoked by the channel layer when someone calls:
        # await channel_layer.group_send(
        #     f"user_{user_id}",
        #     {"type": "send_notification", "message": {...}}
        # )

    # @database_sync_to_async
    # def create_notification(self, lead, message):
    #     return Notification.objects.create(user=self.user, lead=lead, message=message)

    
