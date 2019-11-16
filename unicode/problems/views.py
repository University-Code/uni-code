import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.forms import modelformset_factory
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Problem, ProblemTestCase
from .forms import ProblemForm


def index(request):

    ''' displays the landing page '''

    context = {
            "title": "Welcome to Uni-Code",
            "has": {"dummy":"yes"}
        }
    return render(request, 'problems/index.html', context)


@login_required  
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
        problem.creator = request.user
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




def problems(request):
    ''' 
    Handles pagination of list problems to solve.
    '''

    problems = []
    
    if request.user.is_authenticated:
        for problem in Problem.objects.all():
            problems.append(problem.to_dict(user=request.user))
    else:
        problems = Problem.objects.all()

    paginator = Paginator(problems, 10)
    page = request.GET.get('page')
    problems = paginator.get_page(page)

    return render(request, 'problems/problem_list.html', {'problems': problems})



def upvote_problem(request):

    if request.method == 'GET':

        # returns failure message is 
        if not request.user.is_authenticated:
            return HttpResponse("not authenticated")

        data = request.GET
        print('problem', data['prob_id'], data['upvoted'])
        if data['upvoted'] == "true":
            upvoted = True
        else:
            upvoted = False

        try:
            problem = Problem.objects.get(pk=data['prob_id'])
            problem.set_upvoted(user=request.user, upvoted=upvoted)
        except:
            return HttpResponse(response=404)
        # response for no content
        return HttpResponse("upvoted success")
    return HttpResponse("Failure")