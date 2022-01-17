from django.urls import path
from .views import CheckoutView, checkout_success


app_name = "checkout"

urlpatterns = [
    path('<str:language>', CheckoutView.as_view(), name='checkout'),

    path('success/<str:language>', checkout_success, name='checkout-success'),
]
