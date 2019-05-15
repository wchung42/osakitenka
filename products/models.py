from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


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


# product becomes an orderitem after being added to cart
class OrderItem(models.Model):
	item = models.ForeignKey(Product, on_delete = models.CASCADE)

	def __str__(self):
		return self.title

class Order(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
	items = models.ManyToManyField(OrderItem)
	start_date = models.DateTimeField(auto_now_add = True)
	ordered_date = models.DateTimeField()
	ordered = models.BooleanField(default = False)

	def __str__(self):
		return self.title