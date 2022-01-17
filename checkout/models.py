from django.db import models
from django import forms
from django.conf import settings


class UserMessage(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()


class UserMessageForm(forms.ModelForm):
    message = forms.CharField(required=False, label='Bericht',
                              widget=forms.Textarea(attrs={'placeholder': 'Bericht...', 'class': 'form-control'}))

    class Meta:
        model = UserMessage
        fields = [
            'message'
        ]


class UserMessageFormFR(forms.ModelForm):
    message = forms.CharField(required=False, label='Message',
                              widget=forms.Textarea(attrs={'placeholder': 'Message...', 'class': 'form-control'}))

    class Meta:
        model = UserMessage
        fields = [
            'message'
        ]
