from django.db import models
from django.shortcuts import reverse
from PIL import Image


class Product(models.Model):
    IMG_DIMENSION = 540

    name = models.CharField(max_length=50, default="")
    name_FR = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    description_FR = models.TextField(default="")
    price = models.FloatField()
    image_path = models.CharField(max_length=50, default="")
    total = models.PositiveIntegerField(default=1)
    available = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name

    def get_product_url(self):
        return reverse("products:product-detail", kwargs={
            'pk': self.pk
        })
