from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def cart(request):
 # return HttpResponse("<h1>Services Available</h1>")
 	return render(request,'cart.html',{})

