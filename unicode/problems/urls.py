
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.landing, name='problems-landing'),
    path('playground/',views.playground, name='problems-playground'),
    path('ranked/', views.ranked, name='problems-ranked')
]
