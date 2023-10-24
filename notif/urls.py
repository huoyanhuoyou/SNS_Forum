from django.urls import path, include
from notif import views
from django.urls import re_path

app_name = 'notif'
urlpatterns = [
    path('notifview/<int:notif_id>/', views.notification_view, name='notifview'),
    path('notif/', views.notification_list, name='notiflist'),
    path('notifrm/<int:notif_id>/', views.remove_notification, name='notifrm'),
    path('mark_all_read/', views.mark_all_read, name='notifmar'),
    path('delete_all_read/', views.delete_all_read, name='notifdar'),
    path('user_notifications_count/', views.user_notifications_count, name='notifcount'),
    path('leave_message/', views.leave_message, name='leavemes'),
]
