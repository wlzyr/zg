from django.urls import path

from home.views.channel_v import ChannelList, ADDChannel, DeleteChannel, UpdateChannel

urlpatterns = [
    path('channel/list/', ChannelList.as_view(), name="channel_list"),
    path('channel/add/', ADDChannel.as_view(), name="channel_add"),
    path('channel/delete/', DeleteChannel.as_view(), name="channel_delete"),
    # path('channel/update/', UpdateChannel.as_view(), name="channel_update"),
]
