# Generated by Django 3.2.20 on 2023-07-05 03:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heladeriafrozen', '0002_product_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='discountcode',
            options={'verbose_name': 'Código de descuento', 'verbose_name_plural': 'Códigos de descuento'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Orden de compra', 'verbose_name_plural': 'Ordenes de compra'},
        ),
    ]
