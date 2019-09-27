from django.shortcuts import render, redirect
from . forms import UserRegistrationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(request.POST)
        if registration_form.is_valid():
            registration_form.save()
            username = registration_form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            print("yo")
            return redirect('problems-landing')
            
    else:
        registration_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form' : registration_form})