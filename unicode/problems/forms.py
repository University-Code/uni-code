from django import forms
from .models import Problem, ProblemTestCase

ATTRS = {'cols': '40', 'rows': '5'}
class ProblemForm(forms.ModelForm):

    class Meta:
        model = Problem
        fields = ['title', 'datatype', 'description', 'example_solution']
        widgets = {
                   'description' : forms.Textarea(attrs=ATTRS),
                   'example_solution' : forms.Textarea(attrs=ATTRS)
                  }

class ProblemTestCaseForm(forms.ModelForm):

    class Meta:
        model = ProblemTestCase
        fields = ('test_input', 'test_output')
