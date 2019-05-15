from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Product(models.Model):
	seller = models.ForeignKey(User, related_name='seller', null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=500)
	description = models.CharField(max_length=500, blank=True)
	keywords = models.CharField(max_length=500)
	price = models.DecimalField(max_digits=20, decimal_places=2)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	num_purchased = models.IntegerField(default=0)
	num_viewed = models.IntegerField(default=0)

class ProductsImage(models.Model):
	product = models.ForeignKey(Product, related_name='product', on_delete=models.CASCADE)
	image = models.ImageField(upload_to='product_image', blank=True)