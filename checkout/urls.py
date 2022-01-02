from django.urls import path
from .views import CheckoutView, checkout_success


app_name = "checkout"

urlpatterns = [
    path('', CheckoutView.as_view(), name='checkout'),
    path('success/', checkout_success, name='checkout-success'),
]
