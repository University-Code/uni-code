from django.contrib import admin
from .models import Problem, ProblemTestCase

''' 
    This creates forms at the /admin/ route 
    for easy data entry
'''
admin.site.register(Problem)
admin.site.register(ProblemTestCase)