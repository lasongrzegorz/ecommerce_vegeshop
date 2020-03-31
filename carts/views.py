from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from shop.models import Product
from .models import Cart


def cart_view(request):

	try:
		the_id = request.session['cart_id']
	except:
		the_id = None

	if the_id:
		cart = Cart.objects.get(id=the_id)
		context = {'cart': cart}

		new_total = 0.00
		for item in cart.products.all():
			new_total += float(item.price_gross)
		cart.total = new_total
		cart.save()

	else:
		empty_message = 'Twój koszyk jest pusty'
		context = {'empty': True, 'messages': empty_message}

	template = 'shop/pages/cart.html'
	return render(request, template, context)


def add_to_cart(request, product_id):

	request.session.set_expiry(300)  # Temporarily 5mins

	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id)
	try:
		product = Product.objects.get(id=product_id)
	except Product.DoesNotExist:
		pass
	except:
		pass

	if product not in cart.products.all():
		cart.products.add(product)

	request.session['items_total'] = cart.products.count()

	return HttpResponseRedirect(reverse('shop'))


def remove_from_cart(request, product_id):

	try:
		the_id = request.session['cart_id']
	except:
		new_cart = Cart()
		new_cart.save()
		request.session['cart_id'] = new_cart.id
		the_id = new_cart.id

	cart = Cart.objects.get(id=the_id)

	try:
		product = Product.objects.get(id=product_id)
	except Product.DoesNotExist:
		pass

	if product in cart.products.all():
		cart.products.remove(product)

	request.session['items_total'] = cart.products.count()

	return HttpResponseRedirect(reverse('cart_view'))
