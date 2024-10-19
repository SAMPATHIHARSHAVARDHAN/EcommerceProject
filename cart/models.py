from django.db import models

# Create your models here.
class cart(models.Model):
    id=models.IntegerField(default=0,primary_key="True")
    user_id=models.IntegerField(default="null")
    product_id=models.IntegerField(default="null")
    quantity=models.FloatField(max_length=50,default=0.00)
    rate=models.FloatField(max_length=50,default=0.00)
    ammount=models.FloatField(max_length=50,default=0.00)
    cr_date=models.DateField(default=0)
