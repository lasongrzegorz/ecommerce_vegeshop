from django.db import models
from carts.models import Cart


STATUS_CHOICES = (
	('Started', 'Rozpoczęte'),
	('Preparing', 'W przygotowaniu'),
	('Finished', 'Gotowe'),
)


class Order(models.Model):
	order_id = models.CharField(max_length=120, default='ABC')
	cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return f'Id: {self.id} | {self.order_id}'
