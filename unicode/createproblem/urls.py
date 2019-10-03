from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='createproblem-landing'),
    path('problemtype/',views.problemtype, name='createproblem-problemtype'),
    path('difficulty/', views.difficulty, name='createproblem-difficulty')
]