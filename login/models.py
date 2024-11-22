from django.db import models
from django.utils import timezone


# Create your models here.


class User(models.Model):
    user = models.CharField(max_length=100, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")


class Token(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="用户")
    token = models.CharField(max_length=100, verbose_name="token")
    created_at = models.DateTimeField(default=timezone.now)

    @property
    def is_expired(self):
        return self.created_at < timezone.now() - timezone.timedelta(days=7)
