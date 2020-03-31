from django.shortcuts import render
from .models import Product


def index(request):
	template = 'shop/pages/index.html'
	return render(request, template)


def shop_view(request):
	products = Product.objects.all()
	template = 'shop/pages/shop.html'
	context = {"products": products}
	return render(request, template, context)


def contact_view(request):
	template = 'shop/pages/contact.html'
	return render(request, template)


def about_view(request):
	template = 'shop/pages/about.html'
	return render(request, template)
