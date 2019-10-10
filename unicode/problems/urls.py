
from django.contrib import admin
from django.urls import path, include
from .views import problems_list, create_problem

urlpatterns = [
    path('', problems_list, name='problems'),
    path('create/', create_problem, name='create-problem')
]
