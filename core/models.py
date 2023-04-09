"""
Database models.
"""
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from phone_field import PhoneField
# Create your models here.


class UserManager(BaseUserManager):
    """Manager for User."""
    def create_user(self, email, password=None, **extra_fields):
        """Create, save and return a new user."""
        if not email:
            raise ValueError('User must have an email address.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        """Create and return a new superuser."""
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone = PhoneField(blank=True, help_text='Contact phone number')
    description = models.TextField()
    profile_image = models.ImageField(blank=True,null=True, upload_to = 'profiles/', default = 'profiles/user-default.png')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    @property
    def get_profile_image_url(self):
        try:
            url = self.profile_image.url
        except:
            url =  ''

        return url

    USERNAME_FIELD = 'email'