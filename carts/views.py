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
	else:
		empty_message = 'Twój koszyk jest pusty'
		context = {'empty': True, 'messages': empty_message}

	template = 'shop/pages/cart.html'
	return render(request, template, context)


def update_car(request, product_id):

	request.session.set_expiry(600)  # Temporarily set to 10min
	# to increase quantity each time you hit add to cart
	# qty used in templates as '?qty=<int>'
	try:
		qty = request.GET.get('qty')
		update_qty = True
	except:
		qty = None
		update_qty = False

	# to instantiate new cart per session
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
	cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

	if update_qty and qty:
		if int(qty) == 0:
			cart_item.delete()
			cart.save()
		else:
			cart_item.quantity = int(qty)
			cart_item.save()

	new_total = 0.00
	for item in cart.cartitem_set.all():
		line_total = float(item.product.price_gross) * item.quantity
		new_total += line_total
	cart.total = new_total
	cart.save()

	request.session['items_total'] = cart.cartitem_set.count()

	return HttpResponseRedirect(reverse('shop:shop'))
