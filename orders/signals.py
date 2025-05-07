from django.db.models.signals import post_save
from .models import Order

def update_inventory(sender, instance, **kwargs):
    # Deduct inventory when order is placed
    pass

post_save.connect(update_inventory, sender=Order)