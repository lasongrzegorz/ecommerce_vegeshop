from django.db import models
from shop.models import Product


class Cart(models.Model):
	products = models.ManyToManyField(Product, null=True, blank=True)
	total = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	active = models.BooleanField(default=True)
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return f'Cart id: {self.id}'
