from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from IG.models import IGUser

# custom forms defined here handles user imput

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = IGUser
        fields = ('username', 'email', 'profile_pic')