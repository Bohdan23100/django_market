from django.shortcuts import render,get_object_or_404
from main.models import Product
from user.models import UserData

# Create your views here.

def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    user_data = UserData.objects.filter(user_social=product.user).first()
    return render(request, 'product/product.html', {
        'product': product,
        'user_data': user_data
    })

def cart(request):
    return render(request, 'cart/cart.html')