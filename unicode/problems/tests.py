import unittest

from django.apps import apps
from django.test import TestCase
from problems.apps import ProblemsConfig
from problems.forms import ProblemForm, ProblemTestCaseForm
from problems.models import Problem, ProblemTestCase

# app.py test
class AppsTest(unittest.TestCase):
    def problem_config(self):
        self.assertEqual(ProblemsConfig.name, 'problems')
        self.assertEqual(apps.get_app_config('problems').name, 'problems')

# forms.py test 
'''
class ProblemFormTest(TestCase):

class ProblemTestCaseFormTest(TestCase):    
 '''  

# models.py test
class ProblemModelTest(TestCase):

    #Testing the models.CharField variables as strings
    def test_title_string_representation(self):
        test_title = Problem(title = "This is an Amazing Title!")
        self.assertEqual(str(test_title), test_title.title)
'''
class ProblemTestCaseModelTest(TestCase):

# urls.py test
class UrlsTest(TestCase):

# views.py test
class ViewsTest(TestCase):
'''
