# Generated by Django 3.1.5 on 2021-12-14 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20211214_1005'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familymember',
            old_name='specialRequest',
            new_name='remark',
        ),
    ]
