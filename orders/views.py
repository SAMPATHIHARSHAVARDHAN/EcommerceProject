from django.shortcuts import render

# Create your views here.
def orders(request):
   #return HttpResponse("<h1>Login</h1>")
	 return render(request,'orders.html',{})
