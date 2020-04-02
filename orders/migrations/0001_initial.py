# Generated by Django 3.0.4 on 2020-04-02 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.CharField(default='ABC', max_length=120)),
                ('status', models.CharField(choices=[('Started', 'Rozpoczęte'), ('Finished', 'Zamówione')], default='Started', max_length=120)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carts.Cart')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInvoiceAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('same_as_shipping', models.BooleanField(default=False)),
                ('invoice_company', models.CharField(blank=True, max_length=240, null=True)),
                ('invoice_street', models.CharField(blank=True, max_length=240, null=True)),
                ('invoice_city', models.CharField(blank=True, max_length=120, null=True)),
                ('invoice_zipcode', models.CharField(blank=True, max_length=120, null=True)),
                ('invoice_phone', models.CharField(blank=True, max_length=120, null=True)),
                ('invoice_nip', models.IntegerField(blank=True, null=True)),
                ('invoice_regon', models.IntegerField(blank=True, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
        migrations.CreateModel(
            name='OrderAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('street', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('zipcode', models.CharField(max_length=120)),
                ('phone', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
        ),
    ]
