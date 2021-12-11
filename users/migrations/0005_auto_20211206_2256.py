# Generated by Django 3.1.5 on 2021-12-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20211130_2351'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='family',
            name='invitedToCeremony',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='family',
            name='invitedToDinner',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='family',
            name='invitedToParty',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='family',
            name='invitedToReception',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='family',
            name='language',
            field=models.CharField(choices=[('NL', 'Nederlands'), ('FR', 'Français')], default='NL', max_length=50),
        ),
        migrations.AlterField(
            model_name='family',
            name='address',
            field=models.TextField(),
        ),
    ]