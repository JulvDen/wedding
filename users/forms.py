from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import inlineformset_factory

from .models import Family, FamilyMember


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name',
                                                               'class': 'form-control',
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name',
                                                              'class': 'form-control',
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Email',
                                                           'class': 'form-control',
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password',
                                                                  }))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Password',
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
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']


class UpdateFamilyForm(forms.ModelForm):
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))
    language = forms.ChoiceField(choices=Family.CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Family
        fields = ['address', 'language']


class FamilyMemberForm(forms.ModelForm):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'name',
                                                                        'class': 'form-control', }))
    remark = forms.CharField(max_length=100, required=False,
                                     widget=forms.TextInput(attrs={'placeholder': 'Veggie, allergies,...?',
                                                                   'class': 'form-control', }))
    select_all = forms.BooleanField(required=False, label='Select all')

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
        fields = ['name', 'toCeremony', 'toReception', 'toDinner', 'toParty', 'remark']


FamilyMemberFormSet = inlineformset_factory(Family, FamilyMember, form=FamilyMemberForm, extra=0, can_delete=False)
