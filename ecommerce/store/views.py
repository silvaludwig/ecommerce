from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all() #query into database 
    return render(request, 'home.html', {'products': products})