"""
URL configuration for ecommerce_bd project.

The urlpatterns list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from products.views import addproduct
from cart.views import addcart
from orders.views import place_order

urlpatterns = [
    path('admin/', admin.site.urls),
    path('product/', addproduct.as_view()),
    path('cart/', addcart.as_view()),
    path('order/', place_order.as_view()),
]