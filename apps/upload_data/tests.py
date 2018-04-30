from django.test import TestCase
from django.urls import reverse
from .models import Invoices


class TestsInvoicesViews(TestCase):

    def test_page_upload_200(self):
        url = reverse('upload_data:upload')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)


class TestsInvoicesModel(TestCase):

    def setUp(self):
        self.invoice_insert = Invoices.objects.create(
            purchaser_name='João Silva',
            item_description='R$10 off R$20 of food',
            item_price='10.0',
            purchase_count=2,
            merchant_address='987 Fake St',
            merchant_name="Bob's Pizza",
        )

    def test_insert(self):

        invoice_select = Invoices.objects.get(pk=self.invoice_insert.id)

        self.assertEqual(self.invoice_insert, invoice_select)
