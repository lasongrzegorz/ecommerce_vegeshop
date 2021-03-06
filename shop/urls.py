from django.urls import path, include
from .views import (
    index,
    shop_view,
    shop_vegetables_view,
    shop_fruits_view,
    shop_spices_view,
    shop_others_view,
    contact_view,
    about_view,
)
from carts.views import add_to_cart, get_cartitems_counter
from orders.views import checkout, checkout_sent

app_name = 'shop'

urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop_view, name='shop'),
    path('shop/vegetables/', shop_vegetables_view, name='vegetables'),
    path('shop/fruits/', shop_fruits_view, name='fruits'),
    path('shop/spices/', shop_spices_view, name='spices'),
    path('shop/others/', shop_others_view, name='others'),
    path('shop/add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', include('carts.urls')),
    path('shop/checkout', checkout, name='checkout'),
    path('shop/checkout/sent', checkout_sent, name='checkout_sent'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
    path('shop/session-counter/', get_cartitems_counter, name='get_cartitems_counter')
]
