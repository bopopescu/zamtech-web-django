from django.contrib import admin
from accounts.models import users
from .models import post

# Register your models here.
admin.site.register(users)
admin.site.register(post)