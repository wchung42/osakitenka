# Generated by Django 2.2.1 on 2019-05-15 02:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0024_products_productsimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productsimage',
            name='product',
        ),
        migrations.DeleteModel(
            name='Products',
        ),
        migrations.DeleteModel(
            name='ProductsImage',
        ),
    ]
