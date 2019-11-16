from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.db import models
from problems.models import Problem, ProblemTestCase
from editor.models import UserSubmission
from django.contrib.auth.models import User
from django.core import serializers
from eval_engine.services import eval_setup
import logging, logging.config
import sys

LOGGING = {
    'version': 1,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
        }
    },
    'root': {
        'handlers': ['console'],
        'level': 'INFO'
    }
}

logging.config.dictConfig(LOGGING)
#problem_data= Problem.objects.values()
#logging.info(problem_data)



def editor(request, prob_id):
    ''' 
    Gets the submitted id from url and renders editor.html
    with appropriate data
    '''

    if request.method == "GET":
        try:
            problem = Problem.objects.get(pk=prob_id)
        except:
            # if problem does not exist redirect to playground
            return redirect('playground')

        context = {
            "title": "Editor",
            "problem_title": problem.title,
            "problem_description": problem.description,
            "id": prob_id,
            "has": {"editor":"yes"}
        }

        #logging.info(problem.title)
        #logging.info(problem.description)

        return render(request, 'editor/editor.html', context)

    '''
    User Code Submission 
    '''
    if request.method == "POST":
        response = request.POST

        problem = Problem.objects.get(pk=prob_id)
        current_user= request.user
        language= response['language']
        code= response['code']
        
        #Make user submission object
        user_submission = UserSubmission(submitter=current_user, problem=problem, submission=code, language=language)
        test_cases= ProblemTestCase.objects.filter(problem=problem)
        submission= {"user_submission": user_submission, "test_cases":test_cases}
        #submission.save() ---> NOT saving into database until complely tested
        
        return JsonResponse(eval_setup(submission))


def playground(request):
    context={
        "title": "Editor",
        "has": {"editor":"yes"}
    }
    return render(request, 'editor/editor.html', context)



