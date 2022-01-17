from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import FormView
from django.http import JsonResponse

from products.models import Product
from .models import Order, OrderItem


class OrdersListView(LoginRequiredMixin, ListView):
    context_object_name = 'orders'
    template_name = 'carts/order_list.html'

    def get_queryset(self):
        return self.request.user.order_set.filter(ordered=True)


class OrdersListViewFR(LoginRequiredMixin, ListView):
    context_object_name = 'orders'
    template_name = 'carts/fr/order_list.html'

    def get_queryset(self):
        return self.request.user.order_set.filter(ordered=True)


class CartDetailView(LoginRequiredMixin, DetailView):
    context_object_name = 'order'
    template_name = 'carts/cart.html'

    def get_object(self, queryset=None):
        return self.request.user.order_set.filter(ordered=False).first()


class CartDetailViewFR(LoginRequiredMixin, DetailView):
    context_object_name = 'order'
    template_name = 'carts/fr/cart.html'

    def get_object(self, queryset=None):
        return self.request.user.order_set.filter(ordered=False).first()


class AddToCartAjax(View):
    def post(self, request, product_id, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return JsonResponse({
                'error': 'Om een item toe te voegen dient u aangemeld te zijn.'
            }, status=401)
        if self.request.is_ajax:
            product = get_object_or_404(Product, pk=product_id)
            order, _ = Order.objects.get_or_create(user=self.request.user, ordered=False)
            
            if order.items.filter(item__pk=product_id).exists():
                order_item = order.items.get(item__pk=product_id)
                if product.available <= order_item.quantity:
                    return JsonResponse({'error': 'slechts ' + str(product.available) +
                                                  ' item(s) beschikbaar in stock.'}, status=401)
                order_item.quantity += 1
                order_item.save()
            else:
                if product.available == 0:
                    return JsonResponse({'error': 'Item niet meer in stock.'}, status=401)
                order_item = OrderItem.objects.create(user=self.request.user, item=product)
                order.items.add(order_item)
            return JsonResponse({
                'msg': "Het product werd met success toegevoegd aan winkelmand.",
                'quantity': order_item.quantity,
                'total_items': order.get_total_quantity()
            })


class AddToCartAjaxFR(View):
    def post(self, request, product_id, *args, **kwargs):
        if not self.request.user.is_authenticated:
            return JsonResponse({
                'error': 'Pour ajouter un article il faut être connecté(e).'
            }, status=401)
        if self.request.is_ajax:
            product = get_object_or_404(Product, pk=product_id)
            order, _ = Order.objects.get_or_create(user=self.request.user, ordered=False)

            if order.items.filter(item__pk=product_id).exists():
                order_item = order.items.get(item__pk=product_id)
                if product.available <= order_item.quantity:
                    return JsonResponse({'error': 'seulement ' + str(product.available) +
                                                  ' articles(s) disponible(s) en stock.'}, status=401)
                order_item.quantity += 1
                order_item.save()
            else:
                if product.available == 0:
                    return JsonResponse({'error': 'Article en rupture de stock.'}, status=401)
                order_item = OrderItem.objects.create(user=self.request.user, item=product)
                order.items.add(order_item)
            return JsonResponse({
                'msg': "Le produit a bien été ajouté au panier.",
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
            messages.warning(request, 'Slechts ' + str(product.available) + ' item(s) beschikbaar in stock.')
        else:
            order_item.quantity += 1
            order_item.save()
            messages.success(request, 'Product werd toegevoegd aan winkelmand.')
    else:
        order.items.create(user=request.user, item=product)
        messages.success(request, 'Product werd toegevoegd aan winkelmand.')
    return redirect('carts:show-cart')


@login_required
def increase_product_in_cart_fr(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order, _ = Order.objects.get_or_create(user=request.user, ordered=False)
    if order.items.filter(item__pk=product_id).exists():
        order_item = order.items.get(item__pk=product_id)
        if product.available <= order_item.quantity:
            messages.warning(request, 'Seulement ' + str(product.available) + ' articles(s) disponible(s) en stock.')
        else:
            order_item.quantity += 1
            order_item.save()
            messages.success(request, 'Produit ajouté au panier.')
    else:
        order.items.create(user=request.user, item=product)
        messages.success(request, 'Produit ajouté au panier.')
    return redirect('carts:show-cart-fr')


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
            messages.success(request, 'Product werd uit winkelmand verwijderd.')
        else:
            messages.warning(request, 'Dit product bevindt zich niet in uw winkelmand.')
    else:
        messages.warning(request, 'Winkelmand bestaat niet. Voeg producten toe aan winkelmand.')
        return redirect('products:home-page')
    return redirect('carts:show-cart')

@login_required
def decrease_product_in_cart_fr(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order = Order.objects.filter(user=request.user, ordered=False).first()
    if order:
        order_item = order.items.filter(user=request.user, item=product).first()
        if order_item:
            order_item.quantity -= 1
            order_item.save()
            if order_item.quantity <= 0:
                order.items.remove(order_item)
            messages.success(request, 'Produit retiré du panier.')
        else:
            messages.warning(request, "Ce produit n'est pas dans votre panier.")
    else:
        messages.warning(request, 'Panier inexistant. Ajouter des produits au panier.')
        return redirect('products:home-page-fr')
    return redirect('carts:show-cart-fr')


@login_required
def remove_from_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order = Order.objects.filter(user=request.user, ordered=False).first()
    if order:
        order_item = order.items.filter(user=request.user, item=product).first()
        if order_item:
            order.items.remove(order_item)
            messages.success(request, 'Product werd uit winkelmand verwijderd.')
        else:
            messages.warning(request, 'Dit product bevindt zich niet in uw winkelmand.')
    else:
        messages.warning(request, 'Winkelmand bestaat niet. Voeg producten toe aan winkelmand.')
        return redirect('products:home-page')
    return redirect('carts:show-cart')

@login_required
def remove_from_cart_fr(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    order = Order.objects.filter(user=request.user, ordered=False).first()
    if order:
        order_item = order.items.filter(user=request.user, item=product).first()
        if order_item:
            order.items.remove(order_item)
            messages.success(request, 'Produit retiré du panier.')
        else:
            messages.warning(request, "Ce produit n'est pas dans votre panier.")
    else:
        messages.warning(request, 'Panier inexistant. Ajouter des produits au panier.')
        return redirect('products:home-page-fr')
    return redirect('carts:show-cart-fr')
