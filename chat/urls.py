from django.urls import path, include
from chat import views

app_name = 'chat'
urlpatterns = [
    # 私信发送页面
    path('chat_message/sender:<str:sendername>/receiver:<str:receivername>', views.chat_message, name='chat_message'),
    # 个人信息页面
    path('my_info/<str:username>', views.my_info, name='my_info'),
]
