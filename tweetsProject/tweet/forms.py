from django import forms
from .models import Tweet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class TweetForm(forms.ModelForm):
    class Meta:
        model=Tweet
        fields=['text','user','photo']
        # fields=['text','photo']

class UserRegistrationForm(UserCreationForm):
    # email=forms.EmailField(required=True)
    class Meta:
        model=User
        # fields=('username', 'email', 'password1', 'password2')
        fields=('username','password1','password2')
