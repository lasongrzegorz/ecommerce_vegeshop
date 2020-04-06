from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Product


def index(request):
	template = 'shop/pages/index.html'
	return render(request, template)


def shop_view(request):
	products = Product.objects.all()
	template = 'shop/pages/shop.html'
	context = {"products": products}
	return render(request, template, context)


def shop_vegetables_view(request):
	products = Product.objects.filter(category='Vegetables')
	template = 'shop/pages/shop.html'
	context = {"products": products}
	return render(request, template, context)


def shop_fruits_view(request):
	products = Product.objects.all().filter(category='Fruits')
	template = 'shop/pages/shop.html'
	context = {"products": products}
	return render(request, template, context)


def shop_others_view(request):
	products = Product.objects.all().filter(category='Other')
	template = 'shop/pages/shop.html'
	context = {"products": products}
	return render(request, template, context)


def shop_spices_view(request):
	products = Product.objects.all().filter(category='Spices')
	template = 'shop/pages/shop.html'
	context = {"products": products}
	return render(request, template, context)


def contact_view(request):
	template = 'shop/pages/contact.html'
	return render(request, template)


def about_view(request):
	template = 'shop/pages/about.html'
	return render(request, template)


def search_view(request):
	try:
		q = request.GET.get('q')
	except:
		q = None

	if q:
		products = Product.objects.filter(name__contains=q)
		context = {'query': q, 'products': products}
		template = 'shop/pages/shop.html'
		return render(request, template, context)
	else:
		return redirect(reverse('shop:shop'))
