from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models
from .models import users

# signup form
class signupform(forms.ModelForm):
    full_name = forms.CharField(max_length=128, required=True)
    gender = forms.CharField(widget=forms.RadioSelect(choices=models.gender_choices), max_length=20, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    class Meta:
        model = users # from models.py model
        fields = ('full_name', 'username', 'password', 'email', 'gender') # form fields