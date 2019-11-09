from django import forms
from .models import Problem, ProblemTestCase

class ProblemForm(forms.ModelForm):

    class Meta:
        model = Problem
        fields = ('title', 'description', 'datatype', 'example_solution')


class ProblemTestCaseForm(forms.ModelForm):

    class Meta:
        model = ProblemTestCase
        fields = ('test_input', 'test_output')
