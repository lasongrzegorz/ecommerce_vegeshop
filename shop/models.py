from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


MIN_QUANTITIES = [
	('kg', 'kg'),
	('g', 'g'),
	('pcs', 'szt'),
	('pack', 'op'),
]


class Product(models.Model):
	name = models.CharField(max_length=120)
	description = models.CharField(max_length=240)
	min_qty_value = models.FloatField(default=1)
	min_qty_info = models.CharField(choices=MIN_QUANTITIES, max_length=120)
	net_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	vat = models.FloatField(
		default=0.05,
		validators=[
			MinValueValidator(0),
			MaxValueValidator(1),
		]
	)
	active = models.BooleanField(default=True)
	image = models.ImageField(upload_to='images/', blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	@property
	def price_gross(self):
		return round(float(self.net_price) * (1 + self.vat), 2)

	@property
	def is_image(self):
		if self.image:
			return True
		else:
			return False

	@property
	def vat_rate(self):
		return f'{self.vat * 100}%'
