from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Product, Category
from social_django.models import UserSocialAuth
# Create your views here.

@login_required
def user_products(request):
    try:
        user_social = UserSocialAuth.objects.get(user_id=request.user.id)
        products = Product.objects.filter(user=user_social)
        return render(request, 'user_products/user_products.html', {'products': products})
    except UserSocialAuth.DoesNotExist:
        return render(request, 'user_products/user_products.html', {})

@login_required
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('user_products')

@login_required
def update_product(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = Category.objects.all()
    return render(request, 'update_product/update_product.html', {'product': product, 'categories': categories})

@login_required
def update_product_post(request):
    if request.method == 'POST':
        # togo get data
        id = request.POST.get('id')
        product = Product.objects.get(id=id)
        product.name = request.POST.get('name')
        # bla-bla
        product.save()
        # todo update product
        # todo redirect to user_products