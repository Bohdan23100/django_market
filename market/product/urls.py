from . import views
from django.urls import path

urlpatterns = [
    path('<int:product_id>/', views.product, name='product'),
    path('cart/', views.cart, name='cart'),
]