from django.db import models
from django.shortcuts import reverse
from PIL import Image


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    IMG_DIMENSION = 540

    name = models.CharField(max_length=50, default="")
    name_FR = models.CharField(max_length=50, default="")
    description = models.TextField(default="")
    description_FR = models.TextField(default="")
    price = models.FloatField()
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image_path = models.CharField(max_length=50, default="")
    total = models.PositiveIntegerField(default=1)
    available = models.PositiveIntegerField(default=1)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name

    '''
    def save(self):
        super().save()

        with Image.open(self.thumbnail.path) as img:
            if img.height > self.IMG_DIMENSION or img.width > self.IMG_DIMENSION:
                img.thumbnail((self.IMG_DIMENSION, self.IMG_DIMENSION))
                img.save(self.thumbnail.path)
    '''

    def get_product_url(self):
        return reverse("products:product-detail", kwargs={
            'pk': self.pk
        })
