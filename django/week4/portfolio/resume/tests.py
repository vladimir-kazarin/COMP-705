from django.test import TestCase
from .models import Resume, Experience, Education

# Create your tests here.

class ResumeTestCases(TestCase):

    my_resume = None
    my_education = None
    my_expirience = None

    def setUp(self):
        """
        This runs at the beginning of every single test
        Test database will be deleted at the end of testing automaticaly
        """
        self.my_resume = Resume(first_name='Vladimir', last_name='Kazarin')

        self.my_education = Education.objects.create(
        	institution_name='UNH',
            location='Manchester NH', 
            degree='BS',
            major='CS&E', 
            gpa='3.9'
        )

        self.my_expirience = Experience.objects.create(
            title='QA Engineer',
            company='Snappii',
            location='Rochester NH',
            start_date='2014-05-01',
            end_date='2015-09-01',
            description='Providing quality assurance for 40+ mobile apps.',
        )
        self.my_education.save()
        self.my_expirience.save()
        self.my_resume.save()

    def test_last_name_first(self):
    	"""
        Last name should printed before the first name
        """
        r = Resume.objects.first()
        self.assertEqual(r.last_name_first(), 'Kazarin, Vladimir')

    def test_get_full_name(self):
    	"""
        Test if full name returned correctly
        Last name should follow the first
        """
        r = Resume.objects.first()
        self.assertEqual(r.get_full_name(), 'Vladimir Kazarin')

    def test_get_experience(self):
    	"""
        Test if experience queryset contains correct object
        """
        r = Resume.objects.first()
        self.assertEqual(r.get_experience().first(), self.my_expirience)

    def test_get_education(self):
    	"""
        Test if education queryset contains correct object
        """
        r = Resume.objects.first()
        self.assertEqual(r.get_education().first(), self.my_education)