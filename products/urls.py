from django.urls import path
from django.conf.urls import url
from . import views
from products.views import submit_item, item_list, charge

urlpatterns = [
	path('submit-item/', views.submit_item, name='submit_item'),
	url(r'^item/(?P<pk>\d+)/$', views.view_item, name='view_item'),
	path('search-item/', views.search_item, name='search_item'),
	path('all-items/', views.item_list, name = 'item-list'),
	path('charge/', views.charge, name = 'charge'),
]