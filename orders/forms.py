from django import forms
from .models import OrderAddress, OrderInvoiceAddress
from django.utils.translation import gettext_lazy as _


class OrderAddressForm(forms.ModelForm):
	class Meta:
		model = OrderAddress
		fields = [
			'name',
			'street',
			'city',
			'zipcode',
			'phone',
			'email',
		]

		labels = {
			'name': _('Imię i Nazwisko'),
			'street': _('Ulica'),
			'city': _('Miasto'),
			'zipcode': _('Kod pocztowy'),
			'phone': _('Telefon'),
			'email': _('Email'),
		}


class OrderInvoiceAddressForm(forms.ModelForm):
	class Meta:
		model = OrderInvoiceAddress
		fields = [
			'invoice_company',
			'invoice_street',
			'invoice_city',
			'invoice_zipcode',
			'invoice_phone',
			'invoice_nip',
			'invoice_regon',
		]

		labels = {
			'invoice_company': _('Firma'),
			'invoice_street': _('Ulica'),
			'invoice_city': _('Miasto'),
			'invoice_zipcode': _('Kod pocztowy'),
			'invoice_phone': _('Telefon'),
			'invoice_nip': _('NIP'),
			'invoice_regon': _('Regon'),
		}