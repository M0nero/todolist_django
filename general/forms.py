from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import TextInput, ModelForm

from .models import *


class TodoForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control form-control-lg',
                'type': 'text',
                'id': 'form3'
            })
        }


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form

    username = forms.CharField(max_length=100, label='Username',
                               required=True,
                               widget=forms.TextInput(attrs={'type': 'text',
                                                             'class': 'form-control',
                                                             'id': 'form3Example1c',
                                                             }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'type': 'password',
                                                                  'class': 'form-control',
                                                                  'id': 'form3Example4c',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'type': 'password',
                                                                  'class': 'form-control',
                                                                  'id': 'form3Example4cd',
                                                                  }))

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(required=True, label='Username',
                               widget=forms.TextInput(attrs={'class': 'form-control form-control-lg',
                                                             'type': 'username',
                                                             'id': 'form2Example17'}))
    password = forms.CharField(required=True, label='Password',
                               widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg',
                                                                 'type': 'password',
                                                                 'id': 'form2Example27'}))

    class Meta:
        model = User
        fields = ['username', 'password']
