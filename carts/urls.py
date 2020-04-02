from django.urls import path
from .views import cart_view, remove_from_cart

app_name = 'carts'

urlpatterns = [
    path('', cart_view, name='cart_view'),
    path('remove/<int:id>/', remove_from_cart, name='remove_from_cart'),
]
