from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from shop.models import Product
from .models import Cart, CartItem


def cart_view(request):

	try:
		the_id = request.session['cart_id']
	except:
		the_id = None

	if the_id:
		cart = Cart.objects.get(id=the_id)
		context = {'cart': cart}

		new_total = 0.00
		for item in cart.items.all():
			line_total = float(item.product.price_gross) * item.quantity
			new_total += line_total
		cart.total = new_total
		cart.save()

	else:
		empty_message = 'Twój koszyk jest pusty'
		context = {'empty': True, 'messages': empty_message}

	template = 'shop/pages/cart.html'
	return render(request, template, context)


def update_car(request, product_id):

	request.session.set_expiry(600)  # Temporarily set to 10min
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

	# Returns tuple of ('CartItem object', True/False)
	cart_item, created = CartItem.objects.get_or_create(product=product)
	if created:
		print('created!!!')

	if cart_item not in cart.items.all():
		cart.items.add(cart_item)
	else:
		cart.items.remove(cart_item)

	request.session['items_total'] = cart.items.count()

	return HttpResponseRedirect(reverse('shop:shop'))



# def add_to_cart(request, product_id):
#
# 	request.session.set_expiry(300)  # Temporarily 5mins
#
# 	try:
# 		the_id = request.session['cart_id']
# 	except:
# 		new_cart = Cart()
# 		new_cart.save()
# 		request.session['cart_id'] = new_cart.id
# 		the_id = new_cart.id
#
# 	cart = Cart.objects.get(id=the_id)
# 	try:
# 		product = Product.objects.get(id=product_id)
# 	except Product.DoesNotExist:
# 		pass
# 	except:
# 		pass
#
# 	if product not in cart.products.all():
# 		cart.products.add(product)
#
# 	request.session['items_total'] = cart.products.count()
#
# 	return HttpResponseRedirect(reverse('shop'))
#
#
# def remove_from_cart(request, product_id):
#
# 	try:
# 		the_id = request.session['cart_id']
# 	except:
# 		new_cart = Cart()
# 		new_cart.save()
# 		request.session['cart_id'] = new_cart.id
# 		the_id = new_cart.id
#
# 	cart = Cart.objects.get(id=the_id)
#
# 	try:
# 		product = Product.objects.get(id=product_id)
# 	except Product.DoesNotExist:
# 		pass
#
# 	if product in cart.products.all():
# 		cart.products.remove(product)
#
# 	request.session['items_total'] = cart.products.count()
#
# 	return HttpResponseRedirect(reverse('cart_view'))
