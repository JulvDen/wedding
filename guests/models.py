from django.db import models


class Family(models.Model):
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200)

    def __str__(self):
        return self.name + ' (' + self.head + ')'


class Invitee(models.Model):
    CHOICES = (
        ('XX', '?'),
        ('NL', 'Nederlands'),
        ('FR', 'Français'),
    )
    name = models.CharField(max_length=30, blank=True, default='')
    surname = models.CharField(max_length=200, blank=True, default='')
    email = models.EmailField(max_length=254, blank=True, default='')
    language = models.CharField(max_length=200, choices=CHOICES, default='?')
    ceremony = models.BooleanField()
    reception = models.BooleanField()
    diner = models.BooleanField()
    party = models.BooleanField()
    veggie = models.BooleanField()
    allergy = models.CharField(max_length=200, blank=True, default='')
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    isPlusOne = models.BooleanField()
    present = models.BooleanField()

    def __str__(self):
        if self.name != "":
            return self.name + ' ' + self.surname
        else:
            return "+1"
