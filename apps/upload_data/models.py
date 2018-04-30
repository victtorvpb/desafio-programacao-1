from django.db import models


class Invoices(models.Model):

    purchaser_name = models.CharField(
        max_length=100,
        blank=False,
        null=False)
    item_description = models.CharField(
        max_length=100,
        blank=False,
        null=False)
    item_price = models.FloatField(
        null=False,
        blank=False)
    purchase_count = models.FloatField(
        null=False,
        blank=False
    )
    merchant_address = models.CharField(
        max_length=100,
        blank=False,
        null=False)
    merchant_name = models.CharField(
        max_length=100,
        blank=False,
        null=False)

    def __str__(self):
        return self.purchaser_name
