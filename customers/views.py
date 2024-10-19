from django.shortcuts import render

# Create your views here.

def customers(request):
 # return HttpResponse("<h1>Services Available</h1>")
 	return render(request,'customers.html',{})

