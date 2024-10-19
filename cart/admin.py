from django.contrib import admin
from .models import cart

# Register your models here.
class cartAdmin(admin.ModelAdmin):
    list_display=('id','product_id','user_id','quantity','rate','ammount','cr_date')
    search_fields=('title','content')


admin.site.register(cart , cartAdmin)
