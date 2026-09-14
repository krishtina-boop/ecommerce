from django.db import models
class UserRoleEnum(models.TextChoices):
    ADMIN="admin","Admin"
    CUSTOMER="customer","Customer"