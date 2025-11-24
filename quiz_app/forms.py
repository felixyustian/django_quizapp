from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    nickname = forms.CharField(required=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'nickname'] 
        # Password sudah otomatis ditangani oleh UserCreationForm