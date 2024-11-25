import time

from django.db import models

# Create your models here.
class Channel(models.Model):
    channel_id = models.CharField(max_length=100, verbose_name="频道ID")
    channel_name = models.CharField(max_length=100, verbose_name="频道名称")

    def create_channel(self, channel_name):
        channel_id = time.time()
        Channel.objects.create(channel_id=channel_id, channel_name=channel_name)