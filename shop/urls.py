from django.urls import path, include
from .views import index, shop_view, contact_view, about_view
from carts.views import update_car

app_name = 'shop'

urlpatterns = [
    path('', index, name='home'),
    path('shop/', shop_view, name='shop'),
    path('shop/update_cart/<int:product_id>/', update_car,
         name='update_cart'),
    # path('shop/add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', include('carts.urls')),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name='about'),
]
