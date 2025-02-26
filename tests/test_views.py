from django.test import TestCase, Client
from django.urls import reverse
from digit_ai.models import Project  # adjust import based on your project structure

class DashboardViewTests(TestCase):
    def setUp(self):
        # Create a dummy project and set it as current_project
        self.project = Project.objects.create(name="Test Project", budget=1000, budget_spent=200)
        self.client = Client()
        # Optionally, add more setup like logging in a user if authentication is needed

    def test_dashboard_view_status_code(self):
        response = self.client.get(reverse('dashboard'))
        self.assertEqual(response.status_code, 200)

    def test_dashboard_contains_project_name(self):
        response = self.client.get(reverse('dashboard'))
        self.assertContains(response, self.project.name)
