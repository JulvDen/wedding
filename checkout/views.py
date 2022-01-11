from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail

from products.models import Product
from carts.models import Order
from checkout.models import UserMessage, UserMessageForm
from users.forms import UpdateUserForm

import datetime
from pandas.tseries.offsets import BDay


class CheckoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        order = Order.objects.filter(user=self.request.user, ordered=False).first()
        if not order:
            return redirect('checkout:checkout')
        order_items = order.get_all_items()
        user_form = UpdateUserForm(instance=self.request.user)
        user_message = UserMessage.objects.filter(user=self.request.user, message=True)
        user_message = user_message.first() if user_message.exists() else None
        message_form = UserMessageForm(instance=user_message)
        context = {
            'order': order,
            'user_form': user_form,
            'order_items': order_items,
            'message_form': message_form,
        }
        return render(self.request, 'checkout/checkout.html', context)

    def post(self, *args, **kwargs):
        user_form = UpdateUserForm(self.request.POST, instance=self.request.user)
        message_form = UserMessageForm(self.request.POST)
        order = Order.objects.filter(user=self.request.user, ordered=False).first()

        if user_form.is_valid() and message_form.is_valid():
            user_data = user_form.save(commit=False)
            user_data.user = self.request.user
            user_data.save()

            user_message = message_form.save(commit=False)
            user_message.user = self.request.user
            user_message.save()

            order.user_message = user_message
            order_items = order.get_all_items()

            for item in order_items:
                product = Product.objects.filter(pk=item.item.pk).first()
                product.available = product.available - item.quantity
                product.save()

            order.ordered = True
            order.save()
            print("valid")

        return redirect('checkout:checkout-success')


def checkout_success(request):
    order = Order.objects.filter(user=request.user, ordered=True).order_by('-created').first()
    last_date = datetime.date.today() + BDay(4)
    last_date = last_date.strftime("%d-%m-%Y")
    print(request.user.email)
    send_mail('Bestelling goed ontvangen',
              'Hallo,\n\n'
              'Bedankt voor jouw geschenk! Gelieve ' + str(round(order.get_total_amount(), 2)) +
              ' EUR over te schrijven naar BE33 7360 4003 9846 met vermelding van jouw naam vóór '
               + last_date + '.'
              '\n\nTot Binnenkort!'
              '\n\nGroetjes Lisa & Julien',
              'info@lisa-julien.com',
              [request.user.email],
              fail_silently=False)
    return render(request, 'checkout/success.html', {'datum': last_date})
