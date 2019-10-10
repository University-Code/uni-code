from django.shortcuts import render

<<<<<<< HEAD
def editor(request):
=======
def playground(request):
>>>>>>> bug-fix
    return render(request, 'editor/playground.html', {"title": "Playground"})

# Create your views here.
