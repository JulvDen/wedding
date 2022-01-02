from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, View
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

from products.models import Product
from carts.models import Order
from checkout.models import UserMessage, UserMessageForm


class CheckoutView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        order = Order.objects.filter(user=self.request.user, ordered=False).first()
        if not order:
            return redirect('checkout:checkout')
        order_items = order.get_all_items()
        user_message = UserMessage.objects.filter(user=self.request.user, message=True)
        user_message = user_message.first() if user_message.exists() else None
        form = UserMessageForm(instance=user_message)
        context = {
            'order': order,
            'order_items': order_items,
            'form': form,
        }
        return render(self.request, 'checkout/checkout.html', context)

    def post(self, *args, **kwargs):
        form = UserMessageForm(self.request.POST)
        order = Order.objects.filter(user=self.request.user, ordered=False).first()
        if form.is_valid():
            user_message = form.save(commit=False)
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
                
        return redirect('checkout:checkout-success')


def checkout_success(request):
    send_mail('Bestelling goed ontvangen',
    'Hello there, This is an automated message.',
    'info@lisa-julien.com',
    ['jicef71249@wiicheat.com'],
    fail_silently = False)
    return render(request, 'checkout/success.html')
