from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from main.models import Product, Category
from social_django.models import UserSocialAuth

@login_required
def add_product(request):
    if request.method == 'POST':
        user_social_auth = UserSocialAuth.objects.filter(user=request.user).first()
        if not user_social_auth:
            return render(request, 'add_product/add_product.html', {
                'error': 'Ваша соціальна автентифікація не знайдена.',
                'categories': Category.objects.all()
            })

        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        category_id = request.POST.get('category')

        if not all([name, price, description, image, category_id]):
            return render(request, 'add_product/add_product.html', {
                'error': 'Будь ласка, заповніть усі поля.',
                'categories': Category.objects.all()
            })

        Product.objects.create(
            name=name,
            price=price,
            description=description,
            image=image,
            user=user_social_auth,
            category_id=category_id
        )
        return redirect('add_product')

    return render(request, 'add_product/add_product.html', {
        'categories': Category.objects.all()
    })