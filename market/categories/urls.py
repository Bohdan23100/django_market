from . import views
from django.urls import path

urlpatterns = [
    path('', views.categories, name='categories'),
    path('<int:category_id>/', views.main, name='main'),
]
