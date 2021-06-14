from .models import Comment
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заполни меня'
            })
        }

class AuthForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            'username': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            }),
            'password': TextInput(attrs={
                'type': 'password',
                'class': 'form-control',
                'placeholder': 'Имя пользователя'
            })
        }
