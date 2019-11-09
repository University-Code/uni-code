import unittest

from django.apps import apps
from django.test import TestCase
from users.apps import UsersConfig
from users.forms import UserRegistrationForm
from users.models import Profile

# app.py test
class AppsTest(unittest.TestCase):
    def problem_config(self):
        self.assertEqual(UsersConfig.name, 'users')
        self.assertEqual(apps.get_app_config('users').name, 'users')

'''
# forms.py test
class UserRegistrationFormTest(TestCase):
   
# models.py test
class ProfileModelTest(TestCase):

# views.py test
class ViewsTest(TestCase):
'''