from channels.generic.websocket import JsonWebsocketConsumer
from django.contrib.auth.models import AnonymousUser
from users.utils import get_api_by_user


class GetUserNetwork(JsonWebsocketConsumer):
	def connect(self):
		self.accept()
		if self.scope['user'] and not isinstance(self.scope['user'], AnonymousUser):
			api = get_api_by_user(self.scope['user'])
			self.send(
				{'friends_count': len(api.GetFriends(include_user_entities=False, skip_status=True))}
			)
		else:
			self.send_json(
				{'error': 'You\'re not authorized to access this socket.'}
			)

	def send_json(self, content, close=False):
		pass
