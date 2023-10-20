from users.models import CustomUser
from django.db import models
from django.shortcuts import render

class Message(models.Model):
    sender = models.ForeignKey(CustomUser,related_name='send_messages',on_delete=models.CASCADE,null=True,verbose_name='发送者')
    recipient = models.ForeignKey(CustomUser,related_name='receive_messages',on_delete=models.CASCADE,null=True,verbose_name='接收者')
    create_time = models.DateTimeField(auto_now_add=True,null=True,verbose_name='创建时间')
    message = models.TextField(null=True,verbose_name='消息')
    unread = models.BooleanField(default=True,verbose_name='是否未读')
    objects = models.Manager
    def __str__(self):
        if self.message:
            return self.message

