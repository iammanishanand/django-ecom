from django.shortcuts import render
from .models import Product

def home(request):
    products = Product.objects.all()  # Fetch all products
    context = {'products': products}  # Add to context
    return render(request, 'home.html', context)