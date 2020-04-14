from django.db import models
from shop.models import Product


class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
	quantity = models.FloatField()

	def __str__(self):
		return f'{self.cart.id}'

	def line_total(self):
		return round(self.quantity * self.product.price_gross, 2)


class Cart(models.Model):
	products_total = models.DecimalField(max_digits=200, decimal_places=2, default=0.00)
	delivery_cost = models.DecimalField(max_digits=200, decimal_places=2, default=0.00)
	cart_total = models.DecimalField(max_digits=200, decimal_places=2, default=0.00)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return f'Cart id: {self.id}'

	def get_products_total(self):
		new_products_total = 0
		for item in self.cartitem_set.all():
			line_total = float(item.product.price_gross) * item.quantity
			new_products_total += line_total
		return round(new_products_total, 2)

	def get_delivery_cost(self):
		# Delivery costs set to 15pln unless order > 200pln
		cost = 15
		if self.get_products_total() >= 200:
			cost = 0
		return cost

	def is_min_cart_value(self):
		# Check if order is of minimal value set to 85pln
		valid_order = False
		if self.get_products_total() >= 85:
			valid_order = True
		return valid_order
