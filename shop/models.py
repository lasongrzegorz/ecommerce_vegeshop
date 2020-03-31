from django.db import models


class Product(models.Model):
	name = models.CharField(max_length=120)
	min_qty_value = models.DecimalField(max_digits=100, decimal_places=2, default=0.00)
	min_qty_info = models.CharField(max_length=15)
	net_price = models.DecimalField(max_digits=20, decimal_places=2, default=0.00)
	vat = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	active = models.BooleanField(default=True)
	image = models.ImageField(upload_to='shop/images/', blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	@property
	def price_gross(self):
		return round(self.net_price * (1 + self.vat), 2)

	@property
	def is_image(self):
		if self.image:
			return True
		else:
			return False


class User(models.Model):
	first_name = models.CharField(max_length=60, blank=True)
	last_name = models.CharField(max_length=60, blank=True)
	email = models.EmailField()
	active = models.BooleanField(default=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.email


class Address(models.Model):
	userID = models.ForeignKey(User, on_delete=models.CASCADE)
	street = models.TextField()
	city = models.TextField()
	province = models.TextField()
	code = models.TextField()


def get_deleted_product_id():
	pass


class Order(models.Model):
	userID = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	productID = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
	quantity = models.FloatField()
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.id)
