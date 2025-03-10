from django.shortcuts import render, redirect 
from .models import Product
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms


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
    
def register_user(request):
    form = SignUpForm()

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            # Log in the new user
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.success(request, f"Welcome, {username}!!!")
                return redirect('home')
            else:
                messages.error(request, "There was an issue logging you in after registration.")
                return redirect('login')

        else:
            print(form.errors)  # 🔍 Debugging: Print exact error details
            messages.error(request, "There was an error creating your account. Try again.")
            return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})
