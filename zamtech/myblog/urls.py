from django.urls import path, re_path, include
from accounts import urls

from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.index, name='index'), #main homepage template
    path('accounts', include('accounts.urls', namespace='signout-accounts')), #jumps to other app(accounts)
    path('posting', views.posting, name='posting') #posting url
]