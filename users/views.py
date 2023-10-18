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
                new_user.avatar = form.cleaned_data['avatar']
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
        send_mail('你的验证码', '你的验证码是: ' + code, '813107842@qq.com', [email], fail_silently=False)
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)})