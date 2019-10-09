from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'problems/index.html', {"title": "Welcome to Uni-code"})

def problems_list(request):
    return render(request, 'problems/problems.html', {"title": "Problems"})

def create_problem(request):
    return render(request, 'problems/create.html', {"title": "Create Problem"})

def playground(request):
    return render(request, 'problems/playground.html', {"title": "Playground"})

