# Generated by Django 3.0.4 on 2020-04-02 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('min_qty_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=100)),
                ('min_qty_info', models.CharField(max_length=15)),
                ('net_price', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('vat', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('active', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='shop/images/')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
