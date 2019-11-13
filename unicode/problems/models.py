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
    creator = models.ForeignKey(
        User,
        related_name='problems',
        on_delete=models.SET_NULL,
        null=True,
    )
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    datatype = models.CharField(max_length=10)
    example_solution = models.CharField(max_length=1000)
    datatype = models.CharField(max_length=15, choices=DATATYPE_CHOICES, default='string')
    upvotes = models.ManyToManyField(User, through='Upvote')

    def __str__(self):
        return self.title

    def upvote(self, user):
        Upvote.objects.create(post=self, user=user)

    def set_upvoted(self, user, *, upvoted):
        if upvoted:
            Upvote.objects.get_or_create(problem=self, user=user)
        else:
            self.upvotes.filter(user=user).delete()


class ProblemTestCase(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    test_input = models.CharField(max_length=1000)
    test_output = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.problem} testcase {self.id}'

class Upvote(models.Model):
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='upvotes', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('problem', 'user')