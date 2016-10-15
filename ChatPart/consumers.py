from django.http import HttpResponse
from channels.handler import AsgiHandler

import json
from channels.channel import Group

def ws_connect(message):
	Group('chat').add(message.reply_channel)
	Group('chat').send({'text':'You connect'})

def ws_message(message):
	Group('chat').send({'text': json.dumps({'message': message.content['text'],
                                            'sender': message.reply_channel.name})})

def ws_disconnect(message):
	Group('chat').discard(message.reply_channel)