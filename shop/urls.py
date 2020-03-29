from django.urls import path
from .views import index, shop_view, cart_view, contact_view, about_view

urlpatterns = [
    path('index.html', index, name='index'),
    path('shop.html', shop_view, name='shop'),
    path('cart.html', cart_view, name='cart'),
    path('contact.html', contact_view, name='contact'),
    path('about.html', about_view, name='about'),
]
