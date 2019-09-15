from django.shortcuts import render
from django.http import HttpResponse

def landing(request):
    return render(request, 'problems/base.html', {"title": "Problems"})
def demo(req):
    return render(request, 'problems/base.html', {"title": "Demo"})

def ranked(req):
    return render(request, 'problems/base.html', {"title": "Ranked"})

# Create your views here.
