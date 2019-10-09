from django.shortcuts import render
from django.http import HttpResponse

def playground(request):
    return render(request, 'problems/playground.html', {"title": "Playground"})

# Create your views here.
