# Generated by Django 3.1.5 on 2022-01-05 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='created_date',
            new_name='created',
        ),
    ]
