from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()
class adminside(AbstractUser):
    is_superuser = models.BooleanField(default=False)

    # Add related_name to avoid clashes with default user model
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username