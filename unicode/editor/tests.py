import unittest

from datetime import datetime
from django.apps import apps
from django.test import TestCase
from editor.apps import EditorConfig
from editor.models import UserSubmission

# app.py test
class AppsTest(unittest.TestCase):
    def problem_config(self):
        self.assertEqual(EditorConfig.name, 'editor')
        self.assertEqual(apps.get_app_config('editor').name, 'editor')

# models.py test
class UserSubmissionModelTest(TestCase):
    #def test_submitter(self):


    #def test_problem(self):

    #Testing __str__(self) for the correct string return
    '''
    def test_string_representation(self):
        test_submission = UserSubmission(submitter = "This is my First Submission")
        test_problem = UserSubmission(problem = "This is my First Problem")
        test_language = UserSubmission(language = "Python")
        test_created = UserSubmission(created = "11/6/2019 12:30")
        test_return = test_submission + " - " + test_problem + " - " + test_language + " - " + test_created
        self.assertEqual(str(test_return), UserSubmission.__str__(self))
    '''
    #def test_created(self):
    
    
    #def test_modified(self):        
    
'''
class UrlsTest(TestCase):

class ViewsTest(TestCase):
'''