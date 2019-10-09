
from django.contrib import admin
from django.urls import path, include
from .views import ProblemListView, create_problem

urlpatterns = [
    path('', ProblemListView.as_view(), name='problems'),
    path('create/', create_problem, name='create-problem')

]
