from django.db import models
from entities.models import Entity
from products.models import Product
# from purchases.models import Purchase


class Inflow(models.Model):
    supplier = models.ForeignKey(Entity, on_delete=models.PROTECT, related_name='inflows')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='inflows')
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    batch = models.CharField(max_length=200, blank=True, null=True)
    expiry_date = models.CharField(max_length=200, blank=True, null=True)
    fabrication_date = models.CharField(max_length=200, blank=True, null=True)
    # purchase = models.ForeignKey(Purchase, on_delete=models.PROTECT, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return str(self.product)
