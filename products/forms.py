from django import forms
from django.contrib.auth.models import User
from products.models import Product, ProductsImage

from home.models import Post

class fProducts(forms.ModelForm):
	class Meta:
		model = Product
		fields = (
			'title',
			'description',
			'keywords',
			'price',
			'category',
		)
		def save(self, commit=True):
			item = super(fProducts, self).save(commit=False)
			item.title = self.cleaned_data['title']
			item.description = self.cleaned_data['description']
			item.keywords = self.cleaned_data['keywords']
			item.price = self.cleaned_data['price']
			item.category = self.clean_data['category']

			if commit:
				item.save()

			return item

class fProductsImage(forms.ModelForm):
	class Meta:
		model = ProductsImage
		fields = (
			'image',
		)
		def save(self, commit=True):
			yea = super(fProductsImage, self).save(commit=False)
			yea.image = self.cleaned_data['image']

			if commit:
				yea.save()

			return yea