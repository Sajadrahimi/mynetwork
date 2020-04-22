import os
import urllib
from urllib.request import urlopen, urlretrieve
import uuid

from backend.settings import MEDIA_ROOT
from django.contrib.auth import logout
from django.core.files import File


def social_user(backend, uid, user=None, *args, **kwargs):
	provider = backend.name
	social = backend.strategy.storage.user.get_social_auth(provider, uid)
	if social:
		if user and social.user != user:
			logout(user)
		elif not user:
			user = social.user
	return {'social': social,
			'user': user,
			'is_new': user is None,
			'new_association': social is None}


def get_avatar(backend, uid, user=None, *args, **kwargs):
	try:
		profile_picture_url = kwargs['response']['profile_image_url_https']
		name = profile_picture_url.split('/')[-1]
		content = urlretrieve(profile_picture_url, os.path.join(MEDIA_ROOT, name))
		user.profile_picture.save(
			name,
			File(open(content[0], 'rb'))
		)
		user.save()
	except Exception as e:
		print('!!!!!!!!!!!!!!!!!', e)
