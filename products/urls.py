from django.urls import path

from .views import HomePage, HomePageFR
from .views import ProductDetailView, ProductDetailViewFR


app_name = "products"

urlpatterns = [
    path('', HomePage.as_view(), name='home-page'),
    path('fr', HomePageFR.as_view(), name='home-page-fr'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product/fr/<int:pk>/', ProductDetailViewFR.as_view(), name='product-detail-fr')
]
