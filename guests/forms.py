from django import forms
from .models import Invitee
from django.db.models import Value
from django.db.models.functions import Concat


class InviteeForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(InviteeForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Invitee
        #fields = ("__all__")
        fields = [
            "email",
            "language",
            "ceremony",
            "reception",
            "diner",
            "party",
            "veggie",
        ]