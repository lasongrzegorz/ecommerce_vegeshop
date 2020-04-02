from django.db import models
from carts.models import Cart


STATUS_CHOICES = (
	('Started', 'Rozpoczęte'),
	('Finished', 'Zamówione'),
)


class Order(models.Model):
	order_id = models.CharField(max_length=120, default='ABC')
	cart = models.ForeignKey(Cart, on_delete=models.SET_NULL, blank=True, null=True)
	status = models.CharField(max_length=120, choices=STATUS_CHOICES, default='Started')
	updated = models.DateTimeField(auto_now=True)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __str__(self):
		return f'Id: {self.id} | {self.order_id}'


class OrderAddress(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	name = models.CharField(max_length=120)
	street = models.CharField(max_length=120)
	city = models.CharField(max_length=120)
	zipcode = models.CharField(max_length=120)
	phone = models.CharField(max_length=120)
	email = models.EmailField(max_length=120)

	def __str__(self):
		return f'Zamówienie: {self.order.order_id} | {self.name}'


class OrderInvoiceAddress(models.Model):
	order = models.ForeignKey(Order, on_delete=models.CASCADE)
	invoice_company = models.CharField(max_length=240, blank=True, null=True)
	invoice_street = models.CharField(max_length=240, blank=True, null=True)
	invoice_city = models.CharField(max_length=120, blank=True, null=True)
	invoice_zipcode = models.CharField(max_length=120, blank=True, null=True)
	invoice_phone = models.CharField(max_length=120, blank=True, null=True)
	invoice_nip = models.IntegerField(blank=True, null=True)
	invoice_regon = models.IntegerField(blank=True, null=True)

	def __str__(self):
		return f'Zamówienie: {self.order.order_id} | {self.invoice_company}'
