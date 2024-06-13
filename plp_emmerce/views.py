from django.shortcuts import render
#from django.http import HttpResponse
from .models import Product

# Create your views here.
#def index(request):
   # return HttpResponse("<h1>My first Webpage with python django</h1>")


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products 
    }
    return render(request,'plp_emmerce/product_list.html',context)


