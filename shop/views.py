from django.shortcuts import render


def index(request):
	template = 'shop/pages/index.html'
	return render(request, template)


def shop_view(request):
	template = 'shop/pages/shop.html'
	return render(request, template)


def cart_view(request):
	template = 'shop/pages/cart.html'
	return render(request, template)


def contact_view(request):
	template = 'shop/pages/contact.html'
	return render(request, template)


def about_view(request):
	template = 'shop/pages/about.html'
	return render(request, template)
