from django.contrib.auth.models import AbstractUser
from django.db import models


class UserProfile(AbstractUser):
    phone = models.CharField(max_length=11, verbose_name='手机号码', unique=True)
    avatar = models.ImageField(upload_to='uploads/%y/%m/d', default="")

    class Meta:
        db_table = 'userprofile'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name
