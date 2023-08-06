# models.py
from django.conf import settings
from django.db import models
from chollo_main.models import Product


class CartItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    # Add other fields as needed

    def total_price(self):
        return self.product.price * self.quantity
