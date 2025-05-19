from . import views
from django.urls import path

urlpatterns = [
    path('', views.user_products, name='user_products'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('update/<int:product_id>/', views.update_product, name='update_product'),
    path('update', views.update_product_post, name='update_product_req')
]