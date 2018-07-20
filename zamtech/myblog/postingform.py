from django import forms
from . import models
from .models import post
from django.forms import ModelForm


class postingForm(forms.ModelForm):
    class Meta:
        model = post # submit to post in models.py
        fields = ('title', 'author', 'content')