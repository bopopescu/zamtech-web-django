from django.urls import path, re_path
from django.contrib.auth import authenticate
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
]