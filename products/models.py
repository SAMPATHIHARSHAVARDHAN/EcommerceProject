from django.db import models
 
# Create your models here.
class Products(models.Model):
    product_id=models.IntegerField(default=0)
    product_description=models.CharField(max_length=150,default="null")
    product_type=models.CharField(max_length=150,default="null")
    price=models.FloatField(max_length=50,default=0.00)
    discount=models.FloatField(max_length=50,default=0.00)
    gst=models.FloatField(max_length=50,default=0.00)
    points=models.IntegerField(default=0)
   









