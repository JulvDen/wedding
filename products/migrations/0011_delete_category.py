# Generated by Django 3.1.5 on 2022-01-12 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_remove_product_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Category',
        ),
    ]
