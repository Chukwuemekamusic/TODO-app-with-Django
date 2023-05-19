from django import forms
from django.forms import ModelForm
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        exclude = ['user']
        error_messages = {
            'completed': {
                'required': 'Please indicate whether the task is completed or not.',
            },
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': 'Your title',
                'class': 'form-control rounded-25',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control rounded-25',
            }),
            'due_date': forms.DateTimeInput(attrs={
                'class': 'form-control rounded-25',
                'placeholder': 'YYYY-MM-DD',
            }),
        }


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your username',
        'class': 'form-control rounded-22',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'your email address',
        'class': 'form-control rounded-22',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your password',
        'class': 'form-control rounded-22',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repeat password',
        'class': 'form-control rounded-22',
    }))


class LoginForm(AuthenticationForm):
    """Form definition for Login."""

    class Meta:
        """Meta definition for Loginform."""
        model = User
        fields = ('username', 'password')
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'rounded-8 form-control',
                'placeholder': 'Enter username'
                }),
            'password': forms.PasswordInput(attrs={
                'class': 'rounded-8 form-control',
                'placeholder': 'Enter password'
                }),
        }
