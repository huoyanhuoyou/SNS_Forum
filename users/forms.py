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

class SnoUpdateForm(forms.ModelForm):
 class Meta:
  model = CustomUser
  fields = ['Sno']

class PhoneUpdateForm(forms.ModelForm):
 class Meta:
  model = CustomUser
  fields = ['phone']

class AvatarUpdateForm(forms.ModelForm):
 class Meta:
  model = CustomUser
  fields = ['avatar']
class EmailUpdateForm(forms.ModelForm):
 class Meta:
  model = CustomUser
  fields = ['email']

class NameUpdateForm(forms.ModelForm):
 class Meta:
  model = CustomUser
  fields = ['username']

class VerificationCodeForm(forms.Form):
 verification_code = forms.CharField(max_length=6, label='验证码', required=True)