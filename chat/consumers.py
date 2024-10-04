"""
This is  the file where all the asynchronous functionality will take place.
"""
import json
from channels.generic.websocket import AsyncWebsocketConsumer, WebsocketConsumer

from channels.db import database_sync_to_async
from .models import Message

from users.models import User

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         self.roomGroupName = "group_chat_gfg"
#         await self.channel_layer.group_add(
#             self.roomGroupName,
#             self.channel_name
#         )
#         await self.accept()
#
#     async def disconnect(self, close_code):
#         await self.channel_layer.group_discard(
#             self.roomGroupName,
#             self.channel_layer
#         )
#
#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json["message"]
#         username = text_data_json["username"]
#         await self.channel_layer.group_send(
#             self.roomGroupName, {
#                 "type": "sendMessage",
#                 "message": message,
#                 "username": username,
#             })
#
#     async def sendMessage(self, event):
#         message = event["message"]
#         username = event["username"]
#         await self.send(text_data=json.dumps({"message": message, "username": username}))





class ChatConsumer(AsyncWebsocketConsumer):

    def _room_group_name_generate(self):
        return str(f'chat_{self.scope["user"].id}_{self.recipient_id}'
                    if self.scope["user"].id < self.recipient_id
                    else f'chat_{self.recipient_id}_{self.scope["user"].id}')

    async def connect(self):
        self.recipient_id = self.scope['url_route']['kwargs']['recipient_id']
        self.recipient = await database_sync_to_async(User.objects.get)(pk=self.recipient_id)
        # self.room_group_name = f'chat_{self.scope["user"].id}_{self.recipient_id}'
        self.room_group_name = self._room_group_name_generate()
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data['message']
        await self.save_message(message)
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender': self.scope['user'].username,
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))

    @database_sync_to_async
    def save_message(self, message):
        Message.objects.create(
            sender=self.scope['user'],
            recipient=self.recipient,
            content=message
        )

