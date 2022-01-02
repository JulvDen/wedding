from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators  import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormView
from django.http import JsonResponse

from products.models import Product
from .models import Order, OrderItem


class OrdersListView(LoginRequiredMixin, ListView):
    context_object_name = 'orders'

    def get_queryset(self):
        return self.request.user.order_set.filter(ordered=True)


class CartDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'order'
    template_name = 'carts/cart.html'

    def get_object(self, queryset=None):
        return self.request.user.order_set.filter(ordered=False).first()


class AddToCartAjax(View):
    def post(self, request, product_id, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return JsonResponse({
                'error': 'In order to add item to cart please create an account'
            }, status=401)
        if self.request.is_ajax:
            product = get_object_or_404(Product, pk=product_id)
            order, _ = Order.objects.get_or_create(user=self.request.user, ordered=False)
            
            if order.items.filter(item__pk=product_id).exists():
                order_item = order.items.get(item__pk=product_id)
                if product.available <= order_item.quantity:
                    return JsonResponse({'error': 'Only ' + str(product.available) + ' item(s) left in stock'}, status=401)
                order_item.quantity += 1
                order_item.save()
            else:
                if product.available == 0:
                    return JsonResponse({'error': 'Item out of stock'}, status=401)
                order_item = OrderItem.objects.create(user=self.request.user, item=product)
                order.items.add(order_item)
            return JsonResponse({
                'msg': "Product has been successfully added to cart",
                'quantity': order_item.quantity,
                'total_items': order.get_total_quantity()
            })


@login_required
def increase_product_in_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order, _ = Order.objects.get_or_create(user=request.user, ordered=False)
    if order.items.filter(item__pk=product_id).exists():
        order_item = order.items.get(item__pk=product_id)
        if product.available <= order_item.quantity:
            messages.warning(request, 'Only ' + str(product.available) + ' item(s) left in stock.')
        else:
            order_item.quantity += 1
            order_item.save()
            messages.success(request, 'Product has been added to cart.')
    else:
        order.items.create(user=request.user, item=product)
        messages.success(request, 'Product has been added to cart.')
    return redirect('carts:show-cart')


@login_required
def decrease_product_in_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order = Order.objects.filter(user=request.user, ordered=False).first()
    if order:
        order_item = order.items.filter(user=request.user, item=product).first()
        if order_item:
            order_item.quantity -= 1
            order_item.save()
            if order_item.quantity <= 0:
                order.items.remove(order_item)
            messages.success(request, 'Product has been removed from cart.')
        else:
            messages.warning(request, 'This item is not in your cart.')
    else:
        messages.warning(request, 'Cart does not exists. Add some products to cart.')
        return redirect('products:home-page')
    return redirect('carts:show-cart')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order = Order.objects.filter(user=request.user, ordered=False).first()
    if order:
        order_item = order.items.filter(user=request.user, item=product).first()
        if order_item:
            order.items.remove(order_item)
            messages.success(request, 'Product has been removed from cart.')
        else:
            messages.warning(request, 'This item is not in your cart.')
    else:
        messages.warning(request, 'Cart does not exists. First add products to cart.')
        return redirect('products:home-page')
    return redirect('carts:show-cart')
