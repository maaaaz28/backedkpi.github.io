from multiprocessing.spawn import old_main_modules
from statistics import mode
from unicodedata import category
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils import timezone

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Add your custom fields here

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_groups',
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions',
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )
# class Department(models.Model):
#     name = models.CharField(max_length=250)
#     description = models.TextField(blank=True, null=True)
#     status = models.IntegerField(default = 1)
#     date_added = models.DateTimeField(default=timezone.now)
#     date_updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name

# class Course(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     name = models.CharField(max_length=250)
#     description = models.TextField(blank=True, null=True)
#     status = models.IntegerField(default = 1)
#     date_added = models.DateTimeField(blank=True,null=True)
#     date_updated = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return self.name


