from django.contrib import admin
from django.urls import path
from .views import playground


urlpatterns = [
    path('playground/', playground, name='editor-playground')
]
