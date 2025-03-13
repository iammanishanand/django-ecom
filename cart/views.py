from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse
def cart_summary(request):
    return render(request, "cart_summary.html", {})

def cart_add(request):
    # get the cart
    cart = Cart(request)
    #test for POST
    if request.POST.get('action') =='post':
        #get stuff
        product_id =int(request.POST.get('product_id'))
        #lockup product on the db
        product = get_object_or_404(Product, id=product_id)
        #save it in the session
        cart.add(product=product)

        # Get cart quanity
        cart_quantity = cart.__len__()
        response =JsonResponse({'qty': cart_quantity})

        #return response
        
        # response =JsonResponse({'Product Name': product.name})
        return response
        

def cart_delete(request):
    pass

def cart_update(request):
    pass


