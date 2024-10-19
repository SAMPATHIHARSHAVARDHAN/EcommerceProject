from django.contrib import admin
from .models import order

# Register your models here.
class orderAdmin(admin.ModelAdmin):
    list_display=('id','order_id','product_id','quantity','rate','ammount','status','delivery_date','cr_date')
    search_fields=('title','content')


admin.site.register(order , orderAdmin)
