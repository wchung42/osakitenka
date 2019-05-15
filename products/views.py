from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from .forms import fProducts, fProductsImage, fComment
from products.models import Product, ProductsImage, Comment

from django.conf import settings
import stripe


def submit_item(request):
	if request.method == 'POST':
		form0 = fProducts(request.POST)
		form1 = fProductsImage(request.POST, request.FILES)
		if form0.is_valid() and form1.is_valid():
			item_form = form0.save(commit=False)
			image_form = form1.save(commit=False)
			item_form.seller = request.user
			item_form.save()
			image_form.product = item_form
			image_form.save()
			form0 = fProducts()
			form1 = fProductsImage()
			return redirect('home')
		else:
			return redirect('submit_item')
	else:
		form0 = fProducts()
		form1 = fProductsImage()
		args = {
			'form0': form0,
			'form1': form1,
		}
		return render(request, 'products/submit_item.html', args)

def view_item(request, pk=None):
	this_item = Product.objects.get(pk = pk)
	if pk:
		item = Product.objects.get(pk=pk)
		comments = Comment.objects.filter(parentProduct = item).order_by('-pk')
		item.num_viewed += 1
		item.save()
		img = ProductsImage.objects.filter(product=item)
	else:
		return redirect('home')

	if request.method == 'POST':
		comment_form = fComment(request.POST or None)
		if comment_form.is_valid():
			comment = request.POST.get('comment')
			comments = comments.create(parentProduct = item, user = request.user, comment = comment)
			comments.save()
			return HttpResponseRedirect(request.path_info)
 
	else:
		comment_form = fComment()

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['key'] = settings.STRIPE_PUBLISHABLE_KEY
		return context

	args = {
		'item': item,
		'img': img,
		'comments': comments,
		'fComment': fComment,
		}
	return render(request, 'products/view_item.html', args)

def search_item(request):
		item = Product.objects.all()
		img = ProductsImage.objects.all()
		if request.method == 'POST':
			text = request.POST.get('textfield', None)
			try:
				item = item.filter(title__icontains= text).order_by('-num_purchased', '-num_viewed')
			except:
				return redirect('search_item')
		args = {
			'item': item,
			'img': img,
			}
		return render(request, 'products/search_item.html', args)

def item_list(request):
	context = {
		'items': Product.objects.all()
	}
	return render(request, 'products/item_list.html', context)

def charge(request):
	if request.method == 'POST':
		stripe.api_key = 'sk_test_S00BneclIcn1x8yb9629kfi700vVtyDOhA'
		charge = stripe.Charge.create(
			amount = 500,
			currency = 'usd',
			description = 'Purchased item',
			source=request.POST['stripeToken']
		)
		return render(request, 'products/charge.html')