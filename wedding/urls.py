"""wedding URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

from pages.views import home_view, home_view_fr
from users.views import family, family_fr, CustomLoginView, CustomLoginViewFR
from carts.views import OrdersListView, OrdersListViewFR

from users.forms import LoginForm, LoginFormFR

urlpatterns = [
    path('', home_view, name='home'),
    path('fr', home_view_fr, name='home-fr'),

    path('users/', family, name='users-family'),
    path('users/fr', family_fr, name='users-family-fr'),

    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='login.html',
                                           authentication_form=LoginForm), name='login'),
    path('login/fr', CustomLoginViewFR.as_view(redirect_authenticated_user=True, template_name='fr/login.html',
                                               authentication_form=LoginFormFR), name='login-fr'),
    path('logout/', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('logout/fr', auth_views.LogoutView.as_view(template_name='fr/index.html'), name='logout-fr'),

    path('product/', include('products.urls')),
    path('cart/', include('carts.urls')),
    path('checkout/', include('checkout.urls')),

    path('orders/', OrdersListView.as_view(), name='show-orders'),
    path('orders/fr/', OrdersListViewFR.as_view(), name='show-orders-fr'),

    path('admin/', admin.site.urls),
]

# if settings.DEBUG:
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
