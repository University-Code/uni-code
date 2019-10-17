from django.views.generic.list import ListView
from django.shortcuts import render
from django.http import HttpResponse
from django.forms import modelformset_factory
from .models import Problem, ProblemTestCase
from .forms import ProblemForm

def index(request):
    return render(request, 'problems/index.html', {"title": "Welcome to Uni-code"})

def create_problem(request):
    problem_form = ProblemForm()
    testcase_form = modelformset_factory(ProblemTestCase, fields=('test_input', 'test_output'), extra=3)
    context = {
        'title': 'Create Problem',
        'problem_form': problem_form,
        'testcase_form': testcase_form
    }
    return render(request, 'problems/create.html', context) 



class ProblemListView(ListView):

    model = Problem
    paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
