from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/%Y/%m/%d/', null=True, blank=True,default="path-to-default-avatar.jpg")  # 头像
    Sno = models.CharField(max_length=20, unique=True)  # 学号
    phone = models.CharField(max_length=15, blank=True, null=True)  # 电话
    email = models.EmailField(unique=True, verbose_name="邮箱")

    def __str__(self):
        return 'user{}'.format(self.username)