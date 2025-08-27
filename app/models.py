from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):

    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50)
    user_profile_image = models.ImageField(upload_to="profile")

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = [] 
    objects = UserManager()
    
