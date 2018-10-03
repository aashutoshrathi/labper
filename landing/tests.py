from django.test import TestCase
from . import views


class TestViewTest(TestCase):

    def test_test_view(self):
        self.assertEqual(views.test_func(), True)
