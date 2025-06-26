from django.test import TestCase

# Create your tests here.
class SmapleTestcase(TestCase):
    def test_sample1(self):
        self.assertEqual(1 + 2, 3)