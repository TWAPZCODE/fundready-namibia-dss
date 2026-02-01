from django.test import TestCase
from django.contrib.auth.models import User
from .models import SMEProfile, Assessment

class coreModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')

    def test_sme_profile_creation(self):
        profile = SMEProfile.objects.create(user=self.user, company_name="Test Co", sector="Agriculture")
        self.assertEqual(profile.company_name, "Test Co")

    def test_assessment_creation(self):
        assessment = Assessment.objects.create(user=self.user, score=80)
        self.assertEqual(assessment.score, 80)
