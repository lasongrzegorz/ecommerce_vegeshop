from django.contrib import admin
from .models import Order, OrderAddress, OrderInvoiceAddress

admin.site.register(Order)
admin.site.register(OrderAddress)
admin.site.register(OrderInvoiceAddress)
