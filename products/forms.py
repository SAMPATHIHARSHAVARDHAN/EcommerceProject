from django import forms

class products(forms.Form):
    product_id=forms.IntegerField()
    product_description=forms.CharField(max_length=150)
    product_type=forms.CharField(max_length=150)
    price=forms.FloatField()
    discount=forms.FloatField()
    gst=forms.FloatField()
    points=forms.IntegerField()

