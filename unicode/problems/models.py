from django.db import models
from django.contrib.auth.models import  

# Create your models here.

class Problem(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    example_solution= models.CharField(max_length=1000)
    user_submitted = models.ForeignKey('User')

class ProblemTestCase(models.Model):
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    datatype = models.CharField(max_length=10)
    test_input = models.CharField(max_length=1000)
    test_output = models.CharField(max_length=1000)
    

    
    

  