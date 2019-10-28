from django.shortcuts import render, redirect
from problems.models import Problem

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
