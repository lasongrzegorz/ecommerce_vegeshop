from django.contrib import admin
from .models import Product
from django.utils.translation import ugettext_lazy as _


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
		'vat_rate',
		'price_gross',
		'updated',
	]
	list_editable = [
		'active',
		'net_price',
	]
	list_display_links = ['name']
	list_filter = ['active']
	readonly_fields = ['updated', 'created']

	class Meta:
		model = Product


admin.site.register(Product, ProductAdmin)
