from django.shortcuts import render

def playground(request):
    return render(request, 'editor/playground.html', {"title": "Playground"})

# Create your views here.
