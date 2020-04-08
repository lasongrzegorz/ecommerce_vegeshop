from django.contrib import admin
from .models import Product


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
		'net_price',
	]
	list_display_links = ['name']
	list_filter = ['active', 'category']
	readonly_fields = ['updated', 'created']

	class Meta:
		model = Product

# Changing methods' string representation
	def vat_rate(self, obj):
		return obj.vat_rate()

	def price_gross(self, obj):
		return obj.price_gross

	def is_image(self, obj):
		return obj.is_image

	vat_rate.short_description = 'VAT'
	price_gross.short_description = 'Brutto'
	is_image.short_description = 'Zdjęcie'


admin.site.register(Product, ProductAdmin)
