from django.shortcuts import render, redirect 
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def home(request):
    products = Product.objects.all()  # Fetch all products
    context = {'products': products}  # Add to context
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html', {})

def login_user(request):
    if request.method=="POST":
        username = request.POST['username']
        password = request.POST["password"]
        user= authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            messages.success(request, (f"I know you, {username} Come on in "))
            return redirect ('home')
        else:
            messages.success(request, (f"I do not know you, {username}, please Enter correct Username and Password "))
            return redirect ('login')


    else: 
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request,("You are out!!!"))
    return redirect('home')
    
