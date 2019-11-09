import unittest

from django.apps import apps
from django.test import TestCase
from eval_engine.apps import EvalEngineConfig

# app.py test
class AppsTest(unittest.TestCase):
    def problem_config(self):
        self.assertEqual(EvalEngineConfig.name, 'eval_engine')
        self.assertEqual(apps.get_app_config('eval_engine').name, 'eval_engine')
'''
# models.py test
class ModelsTest(TestCase):
     
# views.py test
class ViewsTest(TestCase):
'''