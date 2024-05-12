from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.

class Client(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    
    groups = models.ManyToManyField(
        Group,
        blank=True,
        related_name='client_groups',  # Use a unique related_name
    )

    user_permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name='client_permissions',  # Use a unique related_name
    )
    