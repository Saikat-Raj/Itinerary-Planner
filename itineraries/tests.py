from django.test import TestCase
from django.urls import reverse


class HomePageTest(TestCase):
    def test_homepage_status_code(self):
        response = self.client.get(reverse("home"))  # Adjust the view name if necessary
        self.assertEqual(
            response.status_code, 200
        )  # Check if the status code is 200 (OK)
