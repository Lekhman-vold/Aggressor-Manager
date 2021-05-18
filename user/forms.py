from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label="username")
    password = forms.CharField(widget=forms.PasswordInput)


class RegisterForm(forms.Form):

    class Meta:
        model = User
        fields = '__all__'
