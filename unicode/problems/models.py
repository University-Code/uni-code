from django.db import models
from django.contrib.auth.models import User

''' Models that represent a unicode problem'''


class Problem(models.Model):
    user_submitted = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    example_solution = models.CharField(max_length=1000)

    def __str__(self):
        return self.title


class ProblemTestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, )
    datatype = models.CharField(max_length=10)
    test_input = models.CharField(max_length=1000)
    test_output = models.CharField(max_length=1000)

    # make tostring
