from django.urls import path, include
from users import views
from django.conf import settings
from django.conf.urls.static import static

# ... 你的其他URL配置 ...


app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),

    path('send_verification_code/', views.send_verification_code, name='send_verification_code')

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)