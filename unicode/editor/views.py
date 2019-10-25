#########################################################  
############ Convert Query Set to Dictionary ############
#########################################################


from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
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
#json = serializers.serialize('json', problem_data)
logging.info(problem_data)


context={
    "title": "Editor",
    "has": {"editor":"yes"},
}

def editor(request):
    return render(request, 'editor/editor.html', context)

# Create your views here.


def test(request):
    response= request.POST

    logging.info(response)
    
    if request.method == "GET":
        return render(request, 'editor/editor.html',context)
    elif request.method == "POST":
        return JsonResponse(response)

    #return HttpsResponse("hello")