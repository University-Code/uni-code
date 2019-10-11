from django.shortcuts import render
context={
    "title": "Editor",
    "has": {"editor":"yes"}
}
def editor(request):
    return render(request, 'editor/editor.html', context)

# Create your views here.
