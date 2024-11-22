from django.db import models


# Create your models here.


class User(models.Model):
    user = models.CharField(max_length=100, verbose_name="用户名")
    password = models.CharField(max_length=100, verbose_name="密码")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
