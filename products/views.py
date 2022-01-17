from django.views.generic import ListView, DetailView
from .models import Product


class HomePage(ListView):
    model = Product
    template_name = 'products/home.html'
    context_object_name = 'products'
    paginate_by = 20


class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_details.html'


class HomePageFR(ListView):
    model = Product
    template_name = 'products/fr/home.html'
    context_object_name = 'products'
    paginate_by = 20


class ProductDetailViewFR(DetailView):
    model = Product
    template_name = 'products/fr/product_details.html'
