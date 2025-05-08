from django.shortcuts import render,get_object_or_404
from main.models import Product

# Create your views here.

def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/product.html', {
        'product': product,
    })

def cart(request):
    return render(request, 'cart/cart.html')