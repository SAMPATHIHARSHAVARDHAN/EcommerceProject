from django.contrib import admin
from .models import Products

# Register your models here.
class ProductsAdmin(admin.ModelAdmin):
    list_display=('product_id','product_description','product_type','price','discount','points','gst')
    search_fields=('title','content')


admin.site.register(Products , ProductsAdmin)



