from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    """docstrUserRegistrationFrom"""
    email = forms.EmailField()

    class Meta(object):
        model = User
        fields = ['username', 'email', 'password1', 'password2']
