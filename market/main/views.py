from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth

@login_required
def index(request):
    # print(request.user)
    # print(request.user.is_authenticated)
    # print(request.user.is_anonymous)
    # print(request.user.is_staff)
    #
    # google_login = request.user.social_auth.get(provider='google-oauth2')
    # print(google_login)
    # extra_data = google_login.extra_data
    # print(extra_data)
    # print(extra_data.get('picture'))
    # print(extra_data.get('email'))
    # print(extra_data.get('locale'))

    products = Product.objects.all()
    return render(request, 'main/index.html', {'products': products})


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'main/product.html', {
        'product': product,
    })


