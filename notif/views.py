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
    messages_list = sorted(messages_list, key=lambda x: x.create_time)
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
    sender_messages = []
    for message in sender_list:
        if message.sender.username not in [msg.sender.username for msg in sender_messages]:
            sender_messages.append(message)

    context = {
        'Sender_info':Sender_info,
        'CustomUser_info': CustomUser_info,
        'sender_messages': sender_messages
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

def post(self, request, to_user):
    if self.request.user.is_authenticated:
        username = self.request.user.username
        if str(username) == str(to_user):
            return redirect(reverse('main'))
        users_img_path = CustomUser.objects.filter(username=username).values('image')[0].get('image')
        message = BeautifulSoup(request.POST.get('message', ''), 'html.parser').get_text()
        if not message:
            return redirect(reverse('chats', args=(to_user,)))
        sender_id = CustomUser.objects.filter(username=username).values()[0].get('id')
        to_user_id = CustomUser.objects.filter(username=to_user).values()[0].get('id')
        to_users_img_path = CustomUser.objects.filter(username=to_user).values('image')
        if to_users_img_path:
            to_users_img_path = to_users_img_path[0].get('image')
        else:

            return redirect(reverse('main'))
        ms = Message.objects.create(sender_id=sender_id, recipient_id=to_user_id, message=message)
        # 以接收者为组名
        group_name = to_user
        # 获取当前频道
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            group_name, {
                'type': 'receive',
                'message': message,
                'recipient': to_user,
                'create_time': str(ms.create_time),
                'sender': username,
                'to_users_img_path': to_users_img_path

            }
        )
