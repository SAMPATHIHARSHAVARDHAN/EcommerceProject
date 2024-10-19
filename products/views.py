from django.shortcuts import render
from django.http import HttpResponse
from products.models import Products
from products.forms import products

# Create your views here.
def home(request):
  data=Products.objects.all()
  product_form=products()
  return render(request,'page-index.html',{ 'product_form':product_form})
  return res


def product(request): 
  # return HttpResponse("<h1>Products Page</h1>")
  data=Products.objects.all()
  product_form=products()
  return render(request,'product.html',{ 'product_form':product_form})
  return res
  

def cart(request):
 # return HttpResponse("<h1>Services Available</h1>")
 	return render(request,'cart.html',{})



def orders(request):
   #return HttpResponse("<h1>Login</h1>")
	 return render(request,'orders.html',{})


def customers(request):
 # return HttpResponse("<h1>Services Available</h1>")
 	return render(request,'customers.html',{})


def login(request):
   #return HttpResponse("<h1>Login</h1>")
	 return render(request,'login.html',{})