from django.db import models
from products.models import Product


class Outflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='outflows')
    unit_cost_price = models.IntegerField()
    unit_selling_price = models.IntegerField()
    quantity = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    # sobrescreve o método save() fazendo com que ele registre o valor unitário a partir do preço de custo e venda do produto
    def save(self, *args, **kwargs):
        unit_cost_price = getattr(self, 'unit_cost_price', False)
        if not unit_cost_price:
            setattr(self, 'unit_cost_price', self.product.cost_price)

        unit_selling_price = getattr(self, 'unit_selling_price', False)
        if not unit_selling_price:
            setattr(self, 'unit_selling_price', self.product.selling_price)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.product)
