from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    registration_form = UserCreationForm()
    return render(request, 'users/register.html', {'form' : registration_form})