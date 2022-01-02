from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required

from .models import Family, FamilyMember

from .forms import RegisterForm, LoginForm
from .forms import UpdateUserForm, UpdateFamilyForm, FamilyMemberFormSet


@login_required
def family(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        family_form = UpdateFamilyForm(request.POST, request.FILES, instance=request.user.family)
        member_formset = FamilyMemberFormSet(request.POST, request.FILES, instance=request.user.family)

        if user_form.is_valid() and family_form.is_valid() and member_formset.is_valid():
            user_form.save()
            family_form.save()
            member_formset.save()
            messages.success(request, 'Your data is updated successfully')
            return redirect(to='users-family')
    else:
        user_form = UpdateUserForm(instance=request.user)
        family_form = UpdateFamilyForm(instance=request.user.family)
        member_formset = FamilyMemberFormSet(instance=request.user.family)

    return render(request, 'users.html', {'user_form': user_form, 'family_form': family_form,
                                          'member_formset': member_formset})


def dispatch(self, request, *args, **kwargs):
    # will redirect to the home page if a user tries to access the register page while logged in
    if request.user.is_authenticated:
        return redirect(to='users/')

    # else process dispatch as it otherwise normally would
    return super(RegisterView, self).dispatch(request, *args, **kwargs)

'''
class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = '../templates/register.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})
'''


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


