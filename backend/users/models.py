from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from users.enums import UserRoleEnum
from users.managers import CustomUserManager
from core.basemodel import BaseModel

class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    email=models.EmailField(unique=True, max_length=255)
    is_staff=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_joined=models.DateTimeField(default=timezone.now)
    name=models.CharField(max_length=200, default="guest")
    role = models.CharField(
        max_length=20,
        choices=UserRoleEnum.choices,
        default=UserRoleEnum.CUSTOMER
    )
    USERNAME_FIELD="email"
    objects = CustomUserManager()
    class Meta:
        ordering = ["id"]
    
    def __str__(self):
        return self.email
    