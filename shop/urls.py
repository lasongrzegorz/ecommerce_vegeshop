from django.urls import path, include
from .views import index, shop_view, contact_view, about_view
from carts.views import add_to_cart
from orders.views import checkout, checkout_sent

app_name = 'shop'

urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop_view, name='shop'),
    path('shop/add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', include('carts.urls')),
    path('shop/checkout', checkout, name='checkout'),
    path('shop/checkout/sent', checkout_sent, name='checkout_sent'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
]
