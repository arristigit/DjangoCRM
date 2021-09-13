from django.test import TestCase
from django.shortcuts import reverse

# Create your tests here.
class LandingPageTest(TestCase):

    def test_status_code(self):
    # To_do some sort of test 
        response = self.client.get(reverse("landing-page"))
        # print(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "landing.html")


    # def test_template_name(self):
    # # To_do some sort of test 
    #     response = self.client.get(reverse("landing-page"))
    #     self.assertTemplateUsed(response, "landing.html")