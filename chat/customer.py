import json

from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message, UserProfile

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


class ChatConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        if self.scope['user'].is_anonymous:
            await self.close()

        else:

            self.group_name = self.scope['user'].username

            await self.channel_layer.group_add(
                self.group_name, self.channel_name
            )

            await self.accept()

    # 离开聊天组
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name, self.channel_name
        )

        await self.close()

    # 接收前端发来的私信消息
    async def receive(self, text_data=None, bytes_data=None):
        print('打印下消息', text_data)
        await self.send(text_data=json.dumps(text_data))