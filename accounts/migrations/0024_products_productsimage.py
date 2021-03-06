# Generated by Django 2.2 on 2019-05-12 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0023_auto_20190512_1546'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.CharField(blank=True, max_length=500)),
                ('keywords', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('num_purchased', models.IntegerField(default=0)),
                ('num_viewed', models.IntegerField(default=0)),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='seller', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProductsImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='product_image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='accounts.Products')),
            ],
        ),
    ]
