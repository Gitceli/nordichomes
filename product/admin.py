from django.contrib import admin

from .models import Category, Product, Make, Area

admin.site.register(Make)
admin.site.register(Category)
admin.site.register(Area)  
admin.site.register(Product)