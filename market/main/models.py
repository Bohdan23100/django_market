from django.db import models
from social_django.models import UserSocialAuth

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to='static/img/product/')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(UserSocialAuth, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)



    def __str__(self):
        return self.name

class Category(models.Model):
    icon = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name