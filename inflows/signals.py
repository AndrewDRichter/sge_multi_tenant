# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver
# from inflows.models import Inflow


# @receiver(signal=post_save, sender=Inflow)
# def inflow_creation_update_product_quantity(sender, instance, created, **kwargs):
#     if created:
#         if instance.quantity > 0:
#             product = instance.product
#             product.quantity += instance.quantity
#             product.save()          

# @receiver(signal=post_delete, sender=Inflow)
# def inflow_deletion_update_product_quantity(sender, instance, **kwargs):
#         product = instance.product
#         if product.quantity > 0:
#             product.quantity -= instance.quantity
#             product.save()  
