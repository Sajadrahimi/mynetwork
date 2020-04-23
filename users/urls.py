from django.urls import path, re_path
from users import consumers
from users.views import GetUserNetwork

# router = DefaultRouter()
# router.register('friends', GetUserNetwork, 'user-network')

urlpatterns = [
	path(r'friends', GetUserNetwork.as_view(), name='user-network'),

]

ws_urlpatterns = [
	re_path(r'ws/friends/$', consumers.GetUserNetwork),
]
