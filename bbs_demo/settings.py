"""
Django settings for bbs_demo project.

Generated by 'django-admin startproject' using Django 4.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os.path
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-z&2a0!of$el(@j7q^5wcu(y%e20hk11=!&dqr+y2+e)s@g%kcb'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 自定义 app
    'bbs',
    'users',
    'chat',
    'notif',

    # 默认添加的 app
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bbs_demo.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bbs_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#配置 MySQL的连接参数
# 配置MySQL数据库连接
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db',  # 数据库名称
        'USER': 'root',        # 数据库用户名
        'PASSWORD': 'bibibibi2219',  # 数据库密码（用单引号或双引号括起来）
        'HOST': 'localhost',   # 数据库主机
        'PORT': '3306',        # 数据库端口（作为字符串）
    }
}





# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# 登录跳转 URL
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'bbs:index'

# 静态文件路径
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

AUTH_USER_MODEL = 'users.CustomUser'


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


# 邮件相关配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'# 发送邮件配置
EMAIL_HOST = 'smtp.qq.com'# 服务器名称
EMAIL_PORT = 465# 服务端口
EMAIL_HOST_USER = '813107842@qq.com' # 填写自己邮箱
EMAIL_HOST_PASSWORD = 'vjvfyrmwnmtybehi'# 在邮箱中设置的客户端授权密码
EMAIL_FROM = 'moxie'# 收件人看到的发件人
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
#EMAIL_USE_TLS = True   #是否使用TLS安全传输协议
EMAIL_USE_SSL = True    #是否使用SSL加密，qq企业邮箱要求使用
