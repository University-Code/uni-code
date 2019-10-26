#########################################################  
############ Convert Query Set to Dictionary ############
#########################################################


from django.shortcuts import render,
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.db import models
from problems.models import Problem
from django.core import serializers
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
problem_data= Problem.objects.values()
logging.info(problem_data)




def test(request):
    response= request.POST
    
    if request.method == "GET":
        return render(request, 'editor/editor.html',context)
    elif request.method == "POST":
        #database

        return JsonResponse(response)

    #return HttpsResponse("hello")




############################################




def editor(request, prob_id):
    ''' 
    Gets the submitted id from url and renders editor.html
    with appropriate data
    '''

    try:
        problem = Problem.objects.get(pk=prob_id)
    except:
        # if problem does not exist redirect to playground
        return redirect('playground')

    context = {
        "title": "Editor",
        "problem_title": problem.title,
        "has": {"editor":"yes"}
    }

    return render(request, 'editor/editor.html', context)


def playground(request):
    context={
        "title": "Editor",
        "has": {"editor":"yes"}
    }
    return render(request, 'editor/editor.html', context)
