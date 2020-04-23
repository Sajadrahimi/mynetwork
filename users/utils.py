from backend.settings import SOCIAL_AUTH_TWITTER_KEY, SOCIAL_AUTH_TWITTER_SECRET
from social_django.models import UserSocialAuth
from twitter import Api
from users.models import Identity


def get_api_by_user(user: Identity) -> Api:
	try:
		user = UserSocialAuth.objects.get(user_id=user.pk)
		oauth_token = user.extra_data.get('access_token').get('oauth_token')
		oauth_token_secret = user.extra_data.get('access_token').get('oauth_token_secret')
		api = Api(consumer_key=SOCIAL_AUTH_TWITTER_KEY,
				  consumer_secret=SOCIAL_AUTH_TWITTER_SECRET,
				  access_token_key=oauth_token,
				  access_token_secret=oauth_token_secret)
		return api

	except UserSocialAuth.DoesNotExist:
		raise ValueError('User is not associated with an social account.')
