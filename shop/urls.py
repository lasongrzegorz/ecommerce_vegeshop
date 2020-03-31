from django.urls import path, include
from .views import index, shop_view, contact_view, about_view
from carts.views import add_to_cart

urlpatterns = [
    path('', index, name='index'),
    path('shop/', shop_view, name='shop'),
    path('shop/add_to_cart/<int:product_id>/', add_to_cart,
         name='add_to_cart'),
    path('cart/', include('carts.urls')),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
]
