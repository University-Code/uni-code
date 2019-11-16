
from django.contrib import admin
from django.urls import path, include
from .views import problems, create_problem, upvote_problem

urlpatterns = [
    path('', problems, name='problems'),
    path('upvote/', upvote_problem),
    path('create/', create_problem, name='create-problem')

]
