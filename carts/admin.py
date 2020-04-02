from django.contrib import admin
from .models import Cart, CartItem


class CartItemAdmin(admin.ModelAdmin):
	list_display = [
		'cart',
		'product',
		'quantity',
	]

	class Meta:
		model = CartItem


admin.site.register(Cart)
admin.site.register(CartItem, CartItemAdmin)