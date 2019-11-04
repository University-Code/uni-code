from django.contrib import admin
from django.urls import path
from .views import *



urlpatterns = [
    path('', playground, name='playground'),
    path('<int:prob_id>', editor, name='editor'),
]
