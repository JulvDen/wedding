from django.urls import path
from .views import increase_product_in_cart, increase_product_in_cart_fr, remove_from_cart, remove_from_cart_fr, \
    decrease_product_in_cart, decrease_product_in_cart_fr, CartDetailView, CartDetailViewFR, \
    AddToCartAjax, AddToCartAjaxFR


app_name = "carts"

urlpatterns = [
    path('', CartDetailView.as_view(), name='show-cart'),
    path('fr', CartDetailViewFR.as_view(), name='show-cart-fr'),

    path('add/<int:product_id>/', AddToCartAjax.as_view(), name='add-to-cart'),
    path('add/fr/<int:product_id>/', AddToCartAjaxFR.as_view(), name='add-to-cart-fr'),

    path('increase/<int:product_id>/', increase_product_in_cart, name='increase-product-in-cart'),
    path('increase/fr/<int:product_id>/', increase_product_in_cart_fr, name='increase-product-in-cart-fr'),

    path('remove/<int:product_id>/', remove_from_cart, name='remove-from-cart'),
    path('remove/fr/<int:product_id>/', remove_from_cart_fr, name='remove-from-cart-fr'),

    path('decrease/<int:product_id>/', decrease_product_in_cart, name='decrease-product-in-cart'),
    path('decrease/fr/<int:product_id>/', decrease_product_in_cart_fr, name='decrease-product-in-cart-fr')
]
