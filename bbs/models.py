from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
# Create your models here.
class Plate(models.Model):
    """板块"""
    text = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.text}'


class Article(models.Model):
    """帖子主体"""
    plate = models.ForeignKey(Plate, on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'articles'

    def __str__(self):
        return f'{self.text[:50]}'


class Comment(models.Model):
    """帖子回复"""
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'comments'

    def __str__(self):
        return f'{self.text[:50]}...'

class Message(models.Model):
    name = models.CharField(max_length=100, null =True)
    email = models.EmailField(null=True)
    timestamp = models.DateTimeField(default = timezone.now)
    content = models.TextField()

    def __str__(self):
        return f'{self.name}({self.email})-{self.timestamp}'
