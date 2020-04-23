from django.shortcuts import render

# Create your views here.
from backend.settings import *
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from social_django.models import UserSocialAuth
from twitter import Api
from twitter.error import TwitterError
from users.serializers import StatusSerializer
from users.utils import get_api_by_user


class GetUserNetwork(APIView):
	permission_classes = [IsAuthenticated, ]

	@method_decorator(cache_page(60 * 60))
	def get(self, request, *args, **kwargs):
		api = get_api_by_user(request.user)
		try:
			friends = api.GetFriends(include_user_entities=False, skip_status=True)

			return Response(
				{'friends': StatusSerializer(friends).data,
				 },
				status=status.HTTP_200_OK
			)
		except TwitterError as e:
			return Response(
				str(e),
				status=status.HTTP_503_SERVICE_UNAVAILABLE
			)
