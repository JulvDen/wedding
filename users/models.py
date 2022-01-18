from django.db import models
from django.contrib.auth.models import User


class Family(models.Model):
    CHOICES = (
        ('NL', 'Nederlands'),
        ('FR', 'Français'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    invitedToCeremony = models.BooleanField(default=False)
    invitedToReception = models.BooleanField(default=False)
    invitedToDinner = models.BooleanField(default=False)
    invitedToParty = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class FamilyMember(models.Model):
    name = models.CharField(max_length=30, blank=True, default='')

    toCeremony = models.BooleanField(blank=True, default=False)
    toReception = models.BooleanField(blank=True, default=False)
    toDinner = models.BooleanField(blank=True, default=False)
    toParty = models.BooleanField(blank=True, default=False)
    remark = models.CharField(max_length=100, blank=True, default='')
    family = models.ForeignKey(Family, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

