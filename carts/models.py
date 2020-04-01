from django.db import models
from shop.models import Product


class CartItem(models.Model):
	cart = models.ForeignKey('Cart', null=True, blank=True, on_delete=models.CASCADE)
	product = models.ForeignKey(Product, null=True, blank=True, on_delete=models.CASCADE)
	quantity = models.IntegerField(default=1)
	line_total = models.DecimalField(max_digits=200, decimal_places=2, default=0.00)

	def __str__(self):
		return f'{self.cart.id}'


class Cart(models.Model):
	# items = models.ManyToManyField(CartItem, null=True, blank=True)
	# products = models.ManyToManyField(Product, null=True, blank=True)
	total = models.DecimalField(max_digits=200, decimal_places=2, default=0.00)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return f'Cart id: {self.id}'
