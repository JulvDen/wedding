# Generated by Django 3.1.5 on 2021-12-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20211208_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='familymember',
            name='toDiner',
        ),
        migrations.AddField(
            model_name='familymember',
            name='toDinner',
            field=models.BooleanField(blank=True, default=False, verbose_name='Diner'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='allergy',
            field=models.CharField(blank=True, default='', max_length=50, verbose_name='Allergies'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='isVeggie',
            field=models.BooleanField(blank=True, default=False, verbose_name='Veggie'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='toCeremony',
            field=models.BooleanField(blank=True, default=False, verbose_name='Ceremony'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='toParty',
            field=models.BooleanField(blank=True, default=False, verbose_name='Party'),
        ),
        migrations.AlterField(
            model_name='familymember',
            name='toReception',
            field=models.BooleanField(blank=True, default=False, verbose_name='Reception'),
        ),
    ]