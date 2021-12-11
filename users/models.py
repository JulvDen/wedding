from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    CHOICES = (
        ('NL', 'Nederlands'),
        ('FR', 'Français'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.TextField(blank=True, default='')
    language = models.CharField(max_length=50, choices=CHOICES, default='NL')

    invitedToCeremony = models.BooleanField(default=False)
    invitedToReception = models.BooleanField(default=False)
    invitedToDinner = models.BooleanField(default=False)
    invitedToParty = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class FamilyMember(models.Model):
    name = models.CharField(max_length=30, blank=True, default='')

    toCeremony = models.BooleanField(blank=True, default=False, verbose_name="Ceremony")
    toReception = models.BooleanField(blank=True, default=False, verbose_name="Reception")
    toDinner = models.BooleanField(blank=True, default=False, verbose_name="Dinner")
    toParty = models.BooleanField(blank=True, default=False, verbose_name="Party")
    isVeggie = models.BooleanField(blank=True, default=False, verbose_name="Veggie")
    allergy = models.CharField(max_length=50, blank=True, default='', verbose_name="Allergies")
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
