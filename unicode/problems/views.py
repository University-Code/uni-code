from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, 'problems/base.html', {"title": "Problems"})
def playground(request):
    return render(request, 'problems/playground.html', {"title": "Playground"})

def ranked(request):
    return render(request, 'problems/base.html', {"title": "Ranked"})

# Create your views here.
