from django.urls import path

from home.views.channel_v import ChannelList

urlpatterns = [
    path('channel/list/', ChannelList.as_view(), name="channel_list"),
]
