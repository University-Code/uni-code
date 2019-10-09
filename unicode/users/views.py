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
            password = registration_form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('problems')
            
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form' : registration_form})



        