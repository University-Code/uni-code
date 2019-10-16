from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('', editor, name='editor'),
    path('test/', test, name='test')
]
