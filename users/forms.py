from django import forms
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):
 avatar = forms.ImageField(required=False)
 Sno = forms.CharField(max_length=50, required=True)
 phone = forms.CharField(max_length=15, required=True)
 email = forms.EmailField(required=True)
 class Meta:
  model = CustomUser
  fields = ("username", "email","Sno","phone","avatar","password1","password2")
