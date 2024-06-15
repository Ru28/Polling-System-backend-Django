import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Poll
from channels.db import database_sync_to_async
from .serializers import PollSerializer

class PollConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.poll_id = self.scope['url_route']['kwargs']['poll_id']
        self.poll_group_name = f'poll_{self.poll_id}'

        await self.channel_layer.group_add(
            self.poll_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.poll_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        poll_id = data['poll_id']
        poll = await self.get_poll(poll_id)

        await self.channel_layer.group_send(
            self.poll_group_name,
            {
                'type': 'poll_vote',
                'poll': poll
            }
        )

    async def poll_vote(self, event):
        poll = event['poll']
        await self.send(text_data=json.dumps({
            'poll': poll
        }))

    @database_sync_to_async
    def get_poll(self, poll_id):
        poll = Poll.objects.get(id=poll_id)
        return PollSerializer(poll).data
