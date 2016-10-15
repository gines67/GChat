from channels.routing import route

channel_routing = {
	'websocket.connect': 'ChatPart.consumers.ws_connect',
	'websocket.receive': 'ChatPart.consumers.ws_message',
	'websocket.disconnect': 'ChatPart.consumers.ws_disconnect',
	#'send_email': 'chat.consumers.send_email_consumer'
}