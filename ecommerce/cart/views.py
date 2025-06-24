from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    totals = cart.get_totals()
    return render(request, 'cart_summary.html', {'cart_products': cart_products, 'cart': cart, 'totals': totals})

def cart_add(request):
    # Get the cart
    cart = Cart(request)

    #test for POST
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)
        # response = JsonResponse({'Product Name: ': product.name})
        cart_quantity = cart.__len__()
        response = JsonResponse({'quantity': cart_quantity})

        
        return response

    return render(request, 'cart_add.html', {})

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.delete(product=product)
        cart_quantity = cart.__len__()
        response = JsonResponse({'quantity': cart_quantity})
        return response


def cart_update(request):
    return render(request, 'cart_update.html', {})

def checkout(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    totals = cart.get_totals()
    return render(request, 'checkout.html', {'cart_products': cart_products, 'cart': cart, 'totals': totals})

