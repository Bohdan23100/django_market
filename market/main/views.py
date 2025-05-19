from django.shortcuts import render, get_object_or_404
from .models import Product



def index(request):
    products = Product.objects.all()[:20]
    return render(request, 'main/index.html', {'products': products})


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'main/product.html', {
        'product': product,
    })


