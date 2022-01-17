from django.db import models
from django.conf import settings
from django import forms

from products.models import Product
from checkout.models import UserMessage


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.item.name}: {self.quantity}'

    def get_total(self):
        return round(self.item.price * self.quantity, 2)


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    payed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    payment_due_date = models.DateField(null=True)
    payment_date = models.DateField(null=True)
    user_message = models.ForeignKey(UserMessage, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username}: {self.get_all_items()}'

    def get_all_items(self):
        return [item for item in self.items.all()]

    def get_total_amount(self):
        total = sum(item.get_total() for item in self.items.all())
        return total

    def get_total_quantity(self):
        return sum(item.quantity for item in self.items.all())
