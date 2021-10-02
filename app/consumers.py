from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async


class PublicChat(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        pass

    async def receive_json(self, content):
        print(content)
        if content['command'] == 'connected':
            await self.channel_layer.group_add(
                'publicchat',
                self.channel_name
            )
            await self.channel_layer.group_send(
                'publicchat',
                {
                    'type': 'm.m',
                    'command': 'user',
                }
            )
        else:
            await self.channel_layer.group_send(
                'publicchat',
                {
                    'type': 'chat.message',
                    'message': content['message'],
                    'user': content['user'],
                    'command': 'received'
                }
            )
        pass

    async def disconnect(self, code):
        await self.channel_layer.group_send(
            'publicchat',
            {
                'type': 'd.m',
                'command': 'user',
            }
        )
        pass

    async def chat_message(self, event):
        await self.send_json({
            'message': event['message'],
            'user': event['user'],
            'command': event['command']
        })

    async def m_m(self, event):
        await self.send_json({
            'command': event['command'],
        })

    async def d_m(self, event):
        await self.send_json({
            'command': event['command'],
        })

