from django.test import TestCase
from .models import Resume

# Create your tests here.
class ResumeTestCases(TestCase):

    def setUp(self):
    	"""
    	This runs at the beginning of every single test
    	Test database will be deleted at the end of testing automaticaly
    	"""
    	my_resume = Resume(first_name='Vladimir', last_name='Kazarin')
    	my_resume.save()

    def test_last_name_first(self):
    	r = Resume.objects.first()
    	self.assertEqual(r.last_name_first(), 'Kazarin Vladimir')
