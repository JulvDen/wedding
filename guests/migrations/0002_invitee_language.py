# Generated by Django 3.1.5 on 2021-09-26 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitee',
            name='Language',
            field=models.CharField(choices=[('NL', 'Nederlands'), ('FR', 'Français')], default='Nederlands', max_length=200),
        ),
    ]