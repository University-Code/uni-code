from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

def register(request):
    if request.method == 'POST': # user is submitting a registry form
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('problems-landing')
            
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form' : registration_form})


def login(request):
    if request.method == 'POST': #user is submitting a login form
        login_form = AuthenticationForm()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            messages.success(request, f'Welcome, {username}')
            return redirect('problems-landing')
    else:
        login_form = AuthenticationForm()
    return render(request, 'users/login.html', {'form' : login_form})
        