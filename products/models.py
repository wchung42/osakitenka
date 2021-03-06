from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MinValueValidator
import decimal
from datetime import datetime
from django.urls import reverse


CATEGORY_CHOICES = (
	('GEN', 'General'),
	('FOO', 'Food'),
	('ELE', 'Electronics'),
	('MISC', 'Misc')
)

# Create your models here.
class Product(models.Model):
	seller = models.ForeignKey(User, related_name='seller', null=True, on_delete=models.SET_NULL)
	title = models.CharField(max_length=500)
	description = models.CharField(max_length=500, blank=True)
	keywords = models.CharField(max_length=500)
	price = models.DecimalField(max_digits=20, decimal_places=2, validators = [MinValueValidator(decimal.Decimal('0.01'))])
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)
	num_purchased = models.IntegerField(default=0)
	num_viewed = models.IntegerField(default=0)
	category = models.CharField(choices = CATEGORY_CHOICES, max_length = 4, default = 'GEN')


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

# comments
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(max_length=255)
    parentProduct = models.ForeignKey(Product, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(default=datetime.now, blank=True)
 
    def __str__(self):
        return '{}-{}'.format(self.product.title, str(self.user.username))
 
    def delete_comment(self):
        self.delete()
 
    def save_comment(self):
        self.save()