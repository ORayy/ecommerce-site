from django.shortcuts import render

# Create your views here.
from .models import Category, Product

def all_products(request):
    products = Product.objects.all()
    return render(request, 'storeApp/home.html', {'products': products})