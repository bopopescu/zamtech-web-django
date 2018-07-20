from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from . import models
from django.contrib.auth import login, authenticate
from .models import users


class loginform(AuthenticationForm):
    username = forms.CharField(max_length=255, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
        model = users # from models.py model
        fields = ('username', 'password') # form fields

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user