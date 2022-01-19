from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import EmailMessage
from django.urls import reverse

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
            if self.kwargs['language'] == "nl":
                return redirect('products:home-page')
            else:
                return redirect('products:home-page-fr')

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
        if self.kwargs['language'] == "nl":
            return render(self.request, 'checkout/checkout.html', context)
        else:
            return render(self.request, 'checkout/fr/checkout.html', context)

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

            order.payment_due_date = datetime.date.today() + BDay(4)
            order.ordered = True
            order.save()

            self.request.session['checkout'] = True

            if self.kwargs['language'] == "nl":
                return redirect('checkout:checkout-success', language="nl")
            else:
                return redirect('checkout:checkout-success', language="fr")


def checkout_success(request, language):
    if 'checkout' in request.session:
        order = Order.objects.filter(user=request.user, ordered=True).order_by('-created').first()
        due_date = order.payment_due_date.strftime("%d-%m-%Y")

        if language == "nl":
            subject = 'Bestelling goed ontvangen'
            content = 'Hallo,\n\n' \
                      'Bedankt voor het cadeau! Gelieve ' + str(round(order.get_total_amount(), 2)) + \
                      ' EUR over te schrijven naar BE33 7360 4003 9846 met vermelding van jouw naam vóór ' \
                      + due_date + '. Als het bedrag tegen dan nog niet is overgemaakt, wordt de bestelling ' \
                      'automatisch geannuleerd en worden de gekozen producten terug beschikbaar worden voor iedereen.' \
                      '\n\nTot Binnenkort!' \
                      '\n\nGroetjes,' \
                      '\n\nLisa & Julien'
        else:
            subject = 'Commande bien reçu'
            content = 'Coucou,\n\n' \
                      'Un tout grand merci pour le cadeau! Merci de bien vouloir faire un virement de ' \
                      + str(round(order.get_total_amount(), 2)) + ' EUR vers le compte BE33 7360 4003 9846 ' \
                      'en mentionnant votre nom et ce avant le ' + due_date + ". Si le montant n'a pas encore été " \
                      "versé d'ici là, la commande sera automatiquement annulée. Les produits que vous avez choisis " \
                      'seront alors à nouveau disponibles pour tout le monde.' \
                      '\n\nÀ Bientôt!' \
                      '\n\nLisa & Julien'

        email = EmailMessage(subject,
                             content,
                             'info@lisa-julien.com',
                             [request.user.email],
                             bcc=['julien-denis@hotmail.com', 'lisaa.pe@hotmail.com']
                             )

        email.send(fail_silently=False)
        del request.session['checkout']
        return render(request, 'checkout/success.html', {'datum': due_date})
    else:
        if language == "nl":
            return redirect('products:home-page')
        else:
            return redirect('products:home-page-fr')