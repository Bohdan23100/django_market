from django.db import models
from social_django.models import UserSocialAuth
# Create your models here.

class UserData(models.Model):
    user_social = models.OneToOneField(UserSocialAuth, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)