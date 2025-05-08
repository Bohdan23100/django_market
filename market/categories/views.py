from django.shortcuts import render
from main.models import Category, Product

# Create your views here.

def categories(request):
    categories = Category.objects.all()
    return render(request, 'categories/categories.html', {'categories': categories})

def main(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    return render(request, 'main/index.html', {'products': products})