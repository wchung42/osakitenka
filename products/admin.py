from django.contrib import admin
from .models import Product, ProductsImage, OrderItem, Order

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductsImage)
admin.site.register(OrderItem)
admin.site.register(Order)