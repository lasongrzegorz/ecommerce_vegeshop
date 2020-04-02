from django.shortcuts import render, redirect
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
		cart.products_total = cart.get_products_total()
		cart.delivery_cost = cart.get_delivery_cost()
		cart.save()
		cart.cart_total = cart.products_total + cart.delivery_cost
		cart.save()

		request.session['items_total'] = cart.cartitem_set.count()
		context = {'cart': cart}
	else:
		empty_message = 'Twój koszyk jest pusty'
		request.session['items_total'] = 0
		context = {'empty': True, 'messages': empty_message}

	template = 'shop/pages/cart.html'
	return render(request, template, context)


def add_to_cart(request, product_id):
	request.session.set_expiry(1200)  # Temporarily set to 20min

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

	if request.method == 'POST':
		qty = request.POST['qty']
		if int(qty) > 0:
			cart_item = CartItem.objects.create(cart=cart, product=product)
			cart_item.quantity = int(qty)
			cart_item.save()

			request.session['items_total'] = cart.cartitem_set.count()

			return redirect(reverse('shop:shop'))
	else:
		return redirect(reverse('shop:shop'))


def remove_from_cart(request, id):
	try:
		the_id = request.session['cart_id']
		# cart = Cart.objects.get(id=the_id)
	except:
		return redirect(reverse('shop:carts:cart_view'))

	cart_item = CartItem.objects.get(id=id)
	cart_item.delete()

	return redirect(reverse('shop:carts:cart_view'))
