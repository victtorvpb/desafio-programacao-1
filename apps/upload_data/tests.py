from django.test import TestCase
from django.urls import reverse

class TestModels(TestCase):

    def test_page_upload_200(self):
        url = reverse('upload_data:upload')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)