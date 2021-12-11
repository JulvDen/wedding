from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Family


@receiver(post_save, sender=User)
def create_family(sender, instance, created, **kwargs):
    if created:
        Family.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_family(sender, instance, **kwargs):
    instance.family.save()
