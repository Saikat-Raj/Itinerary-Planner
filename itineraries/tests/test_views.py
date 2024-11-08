from django.test import TestCase
from django.urls import reverse


class ViewsTestCase(TestCase):
    def test_home_page(self):
        response = self.client.get(
            reverse("home")
        )  # Assuming 'home' is the URL name for your home page
        self.assertEqual(response.status_code, 200)
