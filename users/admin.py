from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

admin.site.register(CustomUser,UserAdmin)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone',)
    fields = ('user','phone',)
    list_display = ('user','Sno',)
    fields = ('user','Sno',)
# Register your models here.