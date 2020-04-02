from django.shortcuts import render, redirect
from django.urls import reverse
from carts.models import Cart
from .models import Order


def checkout(request):

	try:
		the_id = request.session['cart_id']
		cart = Cart.objects.get(id=the_id)
	except Cart.DoesNotExist:
		the_id = None
		return redirect(reverse('shop:carts:cart_view'))

	# returns a tuple of (OrderObject, True/False)
	new_order, created = Order.objects.get_or_create(cart=cart)
	if created:
		new_order.order_id = 'random_id'
		new_order.save()

	if new_order.status == 'Finished':
		del request.session['cart_id']
		return redirect(reverse('shop:carts:cart_view'))

	context = {'order': new_order}
	template = 'shop/pages/checkout.html'

	return render(request, template, context)
