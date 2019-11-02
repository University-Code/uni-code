
from django.contrib import admin
from django.urls import path, include
from .views import problems, create_problem

urlpatterns = [
    path('', problems, name='problems'),
    path('create/', create_problem, name='create-problem')

]
