from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class UserLogin(ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        widgets = {
            'username' : forms.TextInput(attrs={'placeholder' : 'Enter username'}),
            'password' : forms.PasswordInput(attrs={'placeholder' : 'Enter password'})
        }
