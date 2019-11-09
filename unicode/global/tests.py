import unittest

from django.apps import apps
from django.test import TestCase
from apps import GlobalConfig

# app.py test
class AppsTest(unittest.TestCase):
    def problem_config(self):
        self.assertEqual(GlobalConfig.name, 'global')
        self.assertEqual(apps.get_app_config('global').name, 'global')
'''
# models.py test
class ModelsTest(TestCase):

# views.py test
class ViewsTest(TestCase):
'''