from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import inlineformset_factory

from .models import Family, FamilyMember


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               label='Gebruikersnaam',
                               widget=forms.TextInput(attrs={'placeholder': 'Gebruikersnaam',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               label='Wachtwoord',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Wachtwoord',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class LoginFormFR(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               label="Nom d'utilisateur",
                               widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur",
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               label='Mot de passe',
                               widget=forms.PasswordInput(attrs={'placeholder': 'Mot de passe',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email']


class FamilyMemberForm(forms.ModelForm):
    name = forms.CharField(max_length=30, label='Naam', widget=forms.TextInput(attrs={'placeholder': 'name',
                                                                                      'class': 'form-control', }))

    toCeremony = forms.BooleanField(required=False, label='Ceremonie')

    toReception = forms.BooleanField(required=False, label='Receptie')

    toDinner = forms.BooleanField(required=False, label='Diner')

    toParty = forms.BooleanField(required=False, label='Dansfeest')

    select_all = forms.BooleanField(required=False, label='Alles selecteren', widget=forms.CheckboxInput(
        attrs={'class': 'selectAll', }))

    remark = forms.CharField(max_length=100, required=False, label='Opmerkingen',
                             widget=forms.TextInput(attrs={'placeholder': 'Veggie, allergieën,...?',
                                                           'class': 'form-control', }))

    def __init__(self, *args, **kwargs):
        super(FamilyMemberForm, self).__init__(*args, **kwargs)
        if not Family.objects.get(pk=self.instance.family_id).invitedToCeremony:
            del self.fields['toCeremony']  # removes field from form and template
        if not Family.objects.get(pk=self.instance.family_id).invitedToReception:
            del self.fields['toReception']  # removes field from form and template
        if not Family.objects.get(pk=self.instance.family_id).invitedToDinner:
            del self.fields['toDinner']  # removes field from form and template
        if not Family.objects.get(pk=self.instance.family_id).invitedToParty:
            del self.fields['toParty']  # removes field from form and template

    class Meta:
        model = FamilyMember
        fields = ['name', 'toCeremony', 'toReception', 'toDinner', 'toParty', 'select_all', 'remark']


class FamilyMemberFormFR(forms.ModelForm):
    name = forms.CharField(max_length=30, label='Nom', widget=forms.TextInput(attrs={'placeholder': 'name',
                                                                                      'class': 'form-control', }))

    toCeremony = forms.BooleanField(required=False, label='Céremonie')

    toReception = forms.BooleanField(required=False, label='Reception')

    toDinner = forms.BooleanField(required=False, label='Dîner')

    toParty = forms.BooleanField(required=False, label='Soirée Dansante')

    select_all = forms.BooleanField(required=False, label='Sélectionner Tout', widget=forms.CheckboxInput(
        attrs={'class': 'selectAll', }))

    remark = forms.CharField(max_length=100, required=False, label='Remarques',
                             widget=forms.TextInput(attrs={'placeholder': 'Végétarien, allergies,...?',
                                                           'class': 'form-control', }))

    def __init__(self, *args, **kwargs):
        super(FamilyMemberFormFR, self).__init__(*args, **kwargs)
        if not Family.objects.get(pk=self.instance.family_id).invitedToCeremony:
            del self.fields['toCeremony']  # removes field from form and template
        if not Family.objects.get(pk=self.instance.family_id).invitedToReception:
            del self.fields['toReception']  # removes field from form and template
        if not Family.objects.get(pk=self.instance.family_id).invitedToDinner:
            del self.fields['toDinner']  # removes field from form and template
        if not Family.objects.get(pk=self.instance.family_id).invitedToParty:
            del self.fields['toParty']  # removes field from form and template

    class Meta:
        model = FamilyMember
        fields = ['name', 'toCeremony', 'toReception', 'toDinner', 'toParty', 'select_all', 'remark']


FamilyMemberFormSet = inlineformset_factory(Family, FamilyMember, form=FamilyMemberForm, extra=0, can_delete=False)

FamilyMemberFormSetFR = inlineformset_factory(Family, FamilyMember, form=FamilyMemberFormFR, extra=0, can_delete=False)
