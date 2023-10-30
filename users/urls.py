from django.urls import path, include
from users import views
from django.conf import settings
from django.conf.urls.static import static

# ... 你的其他URL配置 ...


app_name = 'users'
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register', views.register, name='register'),
    path('send_verification_code/', views.send_verification_code, name='send_verification_code'),
    path('update_sno/', views.update_sno, name='update_sno'),
    path('update_phone/', views.update_phone, name='update_phone'),
    path('update_email/', views.update_email, name='update_email'),
    path('update_name/', views.update_name, name='update_name'),
    path('update_sno/', views.update_sno, name='update_sno'),
    path('update_phone/', views.update_phone, name='update_phone'),
    path('update_email/', views.update_email, name='update_email'),
    path('update_name/', views.update_name, name='update_name'),
    #path('my-image/',views.my_image,name = "my_image")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)