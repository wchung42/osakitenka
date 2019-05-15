from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import UserProfile, UserProfiles, Messages

from home.models import Post

class RegistrationForm(UserCreationForm):
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = (
			'username',
			'first_name',
			'last_name',
			'email',
			'password1',
			'password2',
			)

class ProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfiles
		fields = (
			'address',
			'credit_card_number', 
			'phone_number',
			'image',
			)

		def save(self, commit=True):
			user = super(ProfileForm, self).save(commit=False)
			user.address = self.cleaned_data['address']
			user.credit_card_number = self.cleaned_data['credit_card_number']
			user.phone_number = self.cleaned_data['phone_number']
			user.image = self.cleaned_data['image']

			if commit:
				user.save()

			return user

class EditProfileForm(UserChangeForm):
	
	class Meta:
		model = User
		fields = (
		'first_name',
		'last_name',
		'email',
		'password',
		)

class SearchUser(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': '...',
			}
		))
	
	class Meta:
		model = Post
		fields = (
			'post',
			
		)

class SendMessage(forms.ModelForm):
	post = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': '...',
			}
		))
	
	class Meta:
		model = Messages
		fields = (
			'message',
			
		)

# class fProducts(forms.ModelForm):
# 	class Meta:
# 		model = Products
# 		fields = (
# 			'title',
# 			'description',
# 			'keywords',
# 			'price',
# 		)
# 		def save(self, commit=True):
# 			item = super(fProducts, self).save(commit=False)
# 			item.title = self.cleaned_data['title']
# 			item.description = self.cleaned_data['description']
# 			item.keywords = self.cleaned_data['keywords']
# 			item.price = self.cleaned_data['price']

# 			if commit:
# 				item.save()

# 			return item

# class fProductsImage(forms.ModelForm):
# 	class Meta:
# 		model = ProductsImage
# 		fields = (
# 			'image',
# 		)
# 		def save(self, commit=True):
# 			yea = super(fProductsImage, self).save(commit=False)
# 			yea.image = self.cleaned_data['image']

# 			if commit:
# 				yea.save()

# 			return yea