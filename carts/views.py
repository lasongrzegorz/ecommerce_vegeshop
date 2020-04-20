from django.shortcuts import render, redirect, Http404, HttpResponse
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
		cart_products = []
		for item in cart.cartitem_set.all():
			cart_products.append(item.product.id)

		qty = request.POST['qty']
		if float(qty) > 0:
			if cart_products:
				if product_id in cart_products:
					cart_item = cart.cartitem_set.get(product_id=product_id)
					cart_item.quantity += float(qty)
					cart_item.save()
					request.session['items_total'] = cart.cartitem_set.count()
				else:
					cart_item = CartItem.objects.create(cart=cart, product=product)
					cart_item.quantity = float(qty)
					cart_item.save()
					request.session['items_total'] = cart.cartitem_set.count()
			else:
				cart_item = CartItem.objects.create(cart=cart, product=product)
				cart_item.quantity = float(qty)
				cart_item.save()

				request.session['items_total'] = cart.cartitem_set.count()

			return redirect(reverse('shop:shop'))
	else:
		return redirect(reverse('shop:shop'))


def remove_from_cart(request, id):

	cart_item = CartItem.objects.get(id=id)
	cart_item.delete()

	return redirect(reverse('shop:carts:cart_view'))


def get_cartitems_counter(request):
	if request.is_ajax():
		return HttpResponse(request.session['items_total'])
	else:
		return Http404
