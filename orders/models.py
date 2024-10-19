from django.db import models

# Create your models here.
class order(models.Model):
    id=models.IntegerField(default=0,primary_key="True")
    order_id=models.IntegerField(default="null")
    product_id=models.IntegerField(default="null")
    quantity=models.FloatField(default=0.00)
    rate=models.FloatField(default=0.00)
    ammount=models.FloatField(default=0.00)
    status=models.CharField(max_length=50,default="process pending")
    delivery_date=models.DateField(default="present date")
    cr_date=models.DateField(default="present date")
