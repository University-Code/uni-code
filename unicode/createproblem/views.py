from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    return render(request, 'createproblem/base.html', {"title": "Problems"})
def problemtype(request):
    return render(request, 'createproblem/base.html', {"title": "Problem Type"})
def difficulty(request):
    return render(request, 'createproblem/base.html', {"title": "Difficulty"})
