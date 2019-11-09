from django.db import models
from django.contrib.auth.models import User

''' Models that represent a unicode problem'''

DATATYPE_CHOICES = (
    ('string', 'String'),
    ('int', 'Int'),
    ('float', 'Float'),
    ('array', 'Array'),
    ('matrix', 'Matrix'),
    ('linkedlist', 'Linked List')
)

class Problem(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    datatype = models.CharField(max_length=10)
    example_solution = models.CharField(max_length=1000)
    datatype = models.CharField(max_length=15, choices=DATATYPE_CHOICES, default='string')

    def __str__(self):
        return self.title


class ProblemTestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE, )
    test_input = models.CharField(max_length=1000)
    test_output = models.CharField(max_length=1000)

    
    def __str__(self):
        return f'{self.problem} testcase {self.id}'
    


