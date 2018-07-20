from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.template.loader import render_to_string, engines
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from accounts.signupform import signupform
from accounts.loginform import loginform
from django.contrib import messages
from django.contrib.auth import login

def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            #signup users
            form.save() #save to database
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            #login user
            login(request, user)
            return redirect('/')
    else:
        form = signupform()
    return render(request, 'signup.html', {'form': signupform})

def signin(request):
    if request.method == 'POST':
        form = loginform(data=request.POST)
        if form.is_valid():
            #login users
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')        
    if request.method != 'POST':
        form = loginform()
    return render(request, 'signin.html', {'form': loginform})