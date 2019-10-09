from django.contrib.auth.models import User
from django.db import models
from problems.models import Problem


# Create your models here.
class UserSubmission(models.Model):
    submitted = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    solution = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    
