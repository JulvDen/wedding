# Generated by Django 3.1.5 on 2021-11-30 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_family'),
    ]

    operations = [
        migrations.RenameField(
            model_name='family',
            old_name='head',
            new_name='address',
        ),
        migrations.RemoveField(
            model_name='family',
            name='name',
        ),
    ]
