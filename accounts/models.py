from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from home.models import Friend

from products.models import Product

# Create your models here.
class UserProfiles(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	address = models.CharField(max_length=100, blank=True)
	credit_card_number = models.CharField(max_length=100, blank=True)
	phone_number = models.CharField(max_length=100, blank=True)
	image = models.ImageField(upload_to='profile_image', blank=True)
	items = models.ManyToManyField(Product, blank = True)

	def __str__(self):
		return self.user.username
		
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfiles.objects.create(user=instance)

class Audio(models.Model):
    name = models.CharField(max_length=125)
    audio_file = models.FileField(upload_to='audio', blank=True)

class Messages(models.Model):
	current_user = models.ForeignKey(User, related_name='send_mes', null=True, on_delete=models.SET_NULL)
	friend_user = models.ForeignKey(User, related_name='receive_mes', null=True, on_delete=models.SET_NULL)
	message = models.CharField(max_length=500, blank=True)
	created_date = models.DateTimeField(auto_now_add=True)
	updated_date = models.DateTimeField(auto_now=True)


#UserProfile not in use, no remove yet
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	username = models.CharField(max_length=100, default='')
	first_name = models.CharField(max_length=100, default='')
	last_name = models.CharField(max_length=100, default='')
	email = models.EmailField(max_length=100, default='')
	address = models.CharField(max_length=100, default='')
	credit_card_number = models.CharField(max_length=100, default='')
	phone_number = models.CharField(max_length=100, default='')
	image = models.ImageField(upload_to='profile_image', blank=True)

	USERNAME_FIELD = 'username'
	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
		
post_save.connect(create_profile, sender=User)
