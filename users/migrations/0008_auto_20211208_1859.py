# Generated by Django 3.1.5 on 2021-12-08 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20211208_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familymember',
            name='isVeggie',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='toCeremony',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='toDiner',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='toParty',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='toReception',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
