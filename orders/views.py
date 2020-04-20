from django.shortcuts import render, redirect
from django.urls import reverse
from carts.models import Cart
from .models import Order, OrderAddress, OrderInvoiceAddress
from .forms import OrderAddressForm, OrderInvoiceAddressForm

from .extras import generate_order_id, send_mail_confirmation


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
		new_order.order_id = generate_order_id()
		request.session['order_id'] = new_order.id
		new_order.save()

	if new_order.status == 'Finished':
		del request.session['cart_id']
		return redirect(reverse('shop:carts:cart_view'))

	address_form = OrderAddressForm()
	address_invoice_form = OrderInvoiceAddressForm()
	context = {
		'order': new_order,
		'address_form': address_form,
		'address_invoice_form': address_invoice_form,
	}
	template = 'shop/pages/checkout.html'

	return render(request, template, context)


def checkout_sent(request):

	try:
		order_id = request.session['order_id']
		order_to_send = Order.objects.get(id=order_id)
	except Order.DoesNotExist:
		return redirect(reverse('shop:carts:cart_view'))

	if request.method == 'POST':
		order_address = OrderAddress.objects.create(order=order_to_send)
		address_form = OrderAddressForm(request.POST)
		if address_form.is_valid():
			order_address = OrderAddressForm(request.POST, instance=order_address)
			order_address.save()

		order_invoice_address = OrderInvoiceAddress.objects.create(order=order_to_send)
		invoice_address_form = OrderInvoiceAddressForm(request.POST)
		if invoice_address_form.is_valid():
			order_invoice_address = OrderInvoiceAddressForm(request.POST, instance=order_invoice_address)
			order_invoice_address.save()
	else:
		print('not post request')

	delivery_address = OrderAddress.objects.get(order_id=order_id)
	invoice_details = OrderInvoiceAddress.objects.get(order_id=order_id)
	ordered_products = order_to_send.cart.cartitem_set.all()
	context = {
		'delivery_address': delivery_address,
		'invoice_details': invoice_details,
		'ordered_products': ordered_products,
		'order': order_to_send,
	}
	template = 'shop/pages/checkout_sent.html'

	# # send order details
	# send_mail_confirmation(template, context)

	order_to_send.status = 'Finished'
	if order_to_send.status == 'Finished':
		del request.session['cart_id']
		del request.session['items_total']

	return render(request, template, context)





