from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .models import Family, FamilyMember

from .forms import LoginForm, LoginFormFR
from .forms import UpdateUserForm, FamilyMemberFormSet, FamilyMemberFormSetFR


@login_required
def family(request):
    if request.method == 'POST':
        member_formset = FamilyMemberFormSet(request.POST, request.FILES, instance=request.user.family)

        if member_formset.is_valid():
            member_formset.save()
            messages.success(request, 'Uw gegevens zijn goed geüpdatet')
            return redirect(to='users-family')
    else:
        member_formset = FamilyMemberFormSet(instance=request.user.family)

    return render(request, 'users.html', {'member_formset': member_formset})


@login_required(login_url='/login/fr')
def family_fr(request):
    if request.method == 'POST':
        member_formset = FamilyMemberFormSetFR(request.POST, request.FILES, instance=request.user.family)

        if member_formset.is_valid():
            member_formset.save()
            messages.success(request, 'Vos données ont bien été mises à jour')
            return redirect(to='users-family-fr')
    else:
        member_formset = FamilyMemberFormSetFR(instance=request.user.family)

    return render(request, 'fr/users.html', {'member_formset': member_formset})


class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class CustomLoginViewFR(LoginView):
    form_class = LoginFormFR

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginViewFR, self).form_valid(form)


