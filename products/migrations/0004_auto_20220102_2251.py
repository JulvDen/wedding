# Generated by Django 3.1.5 on 2022-01-02 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20220102_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default='products/Heenreis_L9ruoMo.jpg', upload_to='products/'),
        ),
    ]
