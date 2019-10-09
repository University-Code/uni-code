from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from .models import Problem


def index(request):
    return render(request, 'problems/index.html', {"title": "Welcome to Uni-code"})


def problems_list(request):
    return render(request, 'problems/problems.html', {"title": "Problems"})


def create_problem(request):
    return render(request, 'problems/create.html', {"title": "Create Problem"})


class ProblemListView(ListView):

    model = Problem
    paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
