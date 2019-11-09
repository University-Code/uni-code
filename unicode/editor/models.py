from django.contrib.auth.models import User
from django.db import models
from problems.models import Problem

Language_Options = {
    ('Java', 'Java'),
    ('C', 'C'),
    ('C++', 'C++'),
    ('JavaScript', 'JavaScript'),
    ('C#', 'C#'),
    ('Python', 'Python'),
    ('Clojure', 'Clojure')
}

class UserSubmission(models.Model):
    submitter = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    submission = models.CharField(max_length=1000)
    language = models.CharField(max_length=50, choices=Language_Options, default='Java')
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.submitter} - {self.problem} - {self.language} - ({self.created})'