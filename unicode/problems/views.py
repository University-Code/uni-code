from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import modelformset_factory
from django.contrib import messages
from .models import Problem, ProblemTestCase
from .forms import ProblemForm

def index(request):
    return render(request, 'problems/index.html', {"title": "Welcome to Uni-code"})

def create_problem(request):
    '''
    Handles displaying and validating new problem submission forms.
    '''

    problem_form = ProblemForm()
    TestCaseFormSet = modelformset_factory(ProblemTestCase,
                                           fields=('test_input', 'test_output'),
                                           extra=3)
    testcase_form = TestCaseFormSet(queryset=ProblemTestCase.objects.none()) 

    context = {
        'title': 'Create Problem',
        'problem_form': problem_form,
        'testcase_form': testcase_form
    }
    if request.method == 'GET':
        return render(request, 'problems/create.html', context)

    if request.method == 'POST':
        problem_form = ProblemForm(request.POST)
        testcase_form = TestCaseFormSet(request.POST)       
        err = 'Your problem did not pass your submitted testcases.'
        suc = 'Problem successfully submitted, Thank You.'

        if not problem_form.is_valid() or not testcase_form.is_valid():
            messages.error(request, err)
            return render(request, 'problems/create.html', context)
        
        problem = problem_form.save(commit=False)
        problem.submitted = request.user
        problem.save()

        for form in testcase_form:
            if not form.is_valid():
                messages.error(request, err)
                return render(request, 'problems/create.html', context)
            testcase = form.save(commit=False)
            testcase.problem = problem
            testcase.save()

        messages.success(request, 'Problem successfully submitted, Thank You.')    
        return redirect('create-problem')




class ProblemListView(ListView):

    model = Problem
    paginate_by = 40

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
