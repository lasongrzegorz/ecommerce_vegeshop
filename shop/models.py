from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


MIN_QUANTITIES = [
	('kg', 'kg'),
	('g', 'g'),
	('pcs', 'szt'),
	('pack', 'op'),
	('liter', 'l')
]

PRODUCTS_CATEGORIES = [
	('Vegetables', 'Warzywa'),
	('Fruits', 'Owoce'),
	('Spices', 'Zioła i przyprawy'),
	('Other', 'Inne'),
]


class Product(models.Model):
	name = models.CharField(max_length=120, verbose_name='Nazwa')
	description = models.CharField(max_length=240, null=True, blank=True,
	                               verbose_name='Opis')
	category = models.CharField(max_length=120, choices=PRODUCTS_CATEGORIES,
	                            default='Warzywa', verbose_name='Kategoria')
	min_qty_value = models.FloatField(default=1, verbose_name='Min ilość')
	min_qty_info = models.CharField(choices=MIN_QUANTITIES, max_length=120,
	default='kg', verbose_name='Min waga')
	net_price = models.DecimalField(max_digits=20, decimal_places=2,
	                                default=0.00, verbose_name='Netto')
	vat = models.FloatField(
		default=0.05,
		validators=[
			MinValueValidator(0),
			MaxValueValidator(1),
		],
		verbose_name='VAT',
	)
	active = models.BooleanField(default=True, verbose_name='Aktywny')
	image = models.ImageField(upload_to='images/', blank=True, null=True,
	                          verbose_name='Zdjęcie')
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, verbose_name='Ostatnia '
	                                                           'zmiana')

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
