import os.path

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.http import HttpResponse
import random
import string
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import SnoUpdateForm,PhoneUpdateForm,EmailUpdateForm,NameUpdateForm,VerificationCodeForm,AvatarUpdateForm
from users.models import CustomUser
from django.conf import settings
# Create your views here.
def register(request):
    """注册页面"""
    if request.method != 'POST':
        form = CustomUserCreationForm()
    else:
        print(request.POST)
        print(request.FILES)

        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user_code = request.POST.get('verification_code', '')
            real_code = request.session.get('verification_code', '')
            if user_code != real_code:
                # 处理验证码不匹配的情况...
                messages.error(request, "验证码不匹配，请重试。")
                return render(request, 'registration/register.html')  # 返回到同一注册页面
            else:
                # 处理验证码匹配的情况...
                # ...例如创建用户、登录用户...
                print(form.cleaned_data['avatar'])
                new_user = form.save(commit = False)
                avatar = form.cleaned_data['avatar']
                new_user.avatar = avatar
                #file_path = os.path.join(settings.MEDIA_ROOT, 'avatars', new_user.avatar)
                #new_user.avatar.save(file_path,new_user.avatar)
                new_user.save()

                login(request, new_user)
                messages.success(request, "注册成功！")
                return redirect('bbs:index')
        else:
            print(form.errors)
            return HttpResponse("Sorry,your password is too simple or your account has been used.")
    context = {'form': form}
    return render(request, 'registration/register.html', context)


@csrf_exempt
def send_verification_code(request):
    email = request.POST.get('email', '')
    code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # 存储code到session以便稍后验证
    request.session['verification_code'] = code

    # 发送邮件（在生产环境中应该异步完成）
    try:
        send_mail('你的验证码', '你的验证码是: ' + code, '2307302370@qq.com', [email], fail_silently=False)
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})

@login_required
def update_sno(request):
    if request.method == 'POST':
        form = SnoUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:update_info', username=request.user.username)  # 重定向到用户信息页面
    else:
        form = SnoUpdateForm(instance=request.user)
    return render(request, 'update/update_sno.html', {'form': form})

@login_required
def update_avatar(request):
    if request.method == 'POST':
        # 获取用户上传的头像文件
        new_avatar = request.FILES.get('avatar')
        # 检查用户是否上传了头像
        if new_avatar:
            # 保存新头像到用户的数据库记录
            request.user.avatar = new_avatar
            request.user.save()
            messages.success(request, '头像已更新')
            return redirect('users:update_info', username=request.user.username)  # 重定向到用户信息页面
        else:
            messages.error(request, '请选择一个有效的头像文件')

    return render(request, 'update/update_avatar.html')


@login_required
def update_phone(request):
    if request.method == 'POST':
        form = PhoneUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:update_info', username=request.user.username)  # 重定向到用户信息页面
    else:
        form = PhoneUpdateForm(instance=request.user)
    return render(request, 'update/update_phone.html', {'form': form})

@login_required
def update_email(request):
    """修改email"""
    if request.method == 'POST':
        form = EmailUpdateForm(request.POST,instance=request.user)
        if form.is_valid():
            user_code = request.POST.get('verification_code', '')
            real_code = request.session.get('verification_code', '')
            if user_code != real_code:
                messages.error(request, "验证码不匹配，请重试。")
                return render(request, 'update/update_email.html')  # 返回到同一注册页面
            else:
                # 处理验证码匹配的情况...
                form.save()
                return redirect('users:update_info', username=request.user.username)
    else:
        form = SnoUpdateForm(instance=request.user)
    return render(request, 'update/update_email.html', {'form': form})

@login_required
def update_name(request):
    if request.method == 'POST':
        form = NameUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:update_info', username=request.user.username)  # 重定向到用户信息页面
    else:
        form = NameUpdateForm(instance=request.user)
    return render(request, 'update/update_name.html', {'form': form})

@login_required
def update_info(request, username):
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
    context = {
        'Sender_info':Sender_info,
        'CustomUser_info': CustomUser_info,
    }

    return render(request, 'update/update_info.html', context)
