import logging
from django.shortcuts import render, get_object_or_404, redirect
from users.models import CustomUser
logger = logging.getLogger(__name__)
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from bs4 import BeautifulSoup
from .models import Message
from django.shortcuts import render
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist

def chat_message(request,sendername,receivername):
    sender = CustomUser.objects.get(username=sendername)  # 获取当前登录用户作为发送者
    recipient = CustomUser.objects.get(username=receivername)  # 设置接收者
    if request.method == 'POST':
        message_text = request.POST.get('message', '')  # 获取提交的消息内容
        if message_text:
            message = Message.objects.create(sender=sender, recipient=recipient, message=message_text)
            message.save()  # 保存消息到数据库
    sender_list = Message.objects.filter(sender=sender, recipient=recipient)
    receiver_list = Message.objects.filter(sender=recipient, recipient=sender)
    messages_list = sender_list.union(receiver_list)
    try:
        latest_create_time = sender_list.latest('create_time').create_time
        messages_list = sorted(messages_list, key=lambda x: x.create_time)
        unread_messages = [message for message in messages_list if message.create_time <= latest_create_time]
        for message in unread_messages:
            message.unread = False
    except ObjectDoesNotExist:
        messages_list = messages_list

    messages = {
        'sender': sender,
        'receiver': recipient,
        'messages': messages_list
    }
    return render(request, 'chat.html', messages)



def my_info(request, username):
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        # 处理用户不存在的情况，例如返回错误页面或重定向到其他地方
        pass
    Sender_info={
        'username':request.user.username
    }
    CustomUser_info = {
        'username': user.username,
        'email': user.email,
        'phone':user.phone,
        'Sno':user.Sno,
        'Imag':user.avatar
        # 添加其他需要的字段
    }

    sender_list = Message.objects.filter(recipient=user)
    receiver_list = Message.objects.filter(sender=user)

    sender_messages = []
    for message in sender_list:
        if message.sender.username not in sender_messages:
            sender_messages.append(message.sender.username)
    receiver_messages = []
    for message in receiver_list:
        if message.recipient.username not in receiver_messages:
            receiver_messages.append(message.recipient.username)
    messages = sender_messages
    for message in receiver_messages:
        if message not in messages:
            messages.append(message)
    sender_messages = sender_list.filter(unread=True)
    context = {
        'Sender_info':Sender_info,
        'CustomUser_info': CustomUser_info,
        'sender_messages': sender_messages,
        'receiver_messages':receiver_messages,
        'messages':messages,
    }

    return render(request, 'my_info.html', context)

def user_info(request, username):
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        # 处理用户不存在的情况，例如返回错误页面或重定向到其他地方
        pass
    Sender_info={
        'username':request.user.username
    }
    CustomUser_info = {
        'username': user.username,
        'email': user.email,
        'phone':user.phone,
        'Sno':user.Sno,
        'Imag':user.avatar
        # 添加其他需要的字段
    }

    sender_list = Message.objects.filter(recipient=user)
    sender_messages = []
    for message in sender_list:
        sender_messages.append(message)

    context = {
        'Sender_info':Sender_info,
        'CustomUser_info': CustomUser_info,
        'sender_messages': sender_messages
    }

    return render(request, 'others_info.html', context)

