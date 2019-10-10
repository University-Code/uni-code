from django.contrib import admin
from django.urls import path
from .views import editor


urlpatterns = [
    path('', editor, name='editor')
]
