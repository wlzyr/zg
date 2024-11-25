from django.urls import path

from home.views.channel_v import ChannelList
from login.views.login import CreateUser, Login

urlpatterns = [
    path('create/user/', CreateUser.as_view(), name="create_user"),
    path('login_user/', Login.as_view(), name="login_user"),

    path('channel/list/', ChannelList.as_view(), name="channel_list"),
]
