from django.contrib import admin
from .models import Product, User, Address, Order


class ProductAdmin(admin.ModelAdmin):
	date_hierarchy = 'updated'
	search_fields = ['name']
	list_display = [
		'name',
		'active',
		'is_image',
		'min_qty_value',
		'min_qty_info',
		'net_price',
		'vat',
		'price_gross',
		'updated',
	]
	list_editable = [
		'active',
		'min_qty_value',
		'min_qty_info',
		'net_price',
		'vat',
	]
	# list_display_links = None
	list_filter = ['active']
	readonly_fields = ['updated', 'created']

	class Meta:
		model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(Address)
admin.site.register(Order)
