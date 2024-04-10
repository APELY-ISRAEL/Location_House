from django.contrib.auth.models import AbstractUser, User 
from django.db import models



class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('client', 'Client'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='client')
    admin_id = models.CharField(max_length=20, unique=True, blank=True, null=True)
