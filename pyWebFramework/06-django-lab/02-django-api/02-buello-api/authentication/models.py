from django.db import models

# Create your models here.
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)

from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):

        if username is None:
            raise TypeError('Users must provide a username') 
        
        if not email:
            raise TypeError('Users must have an email address')

        
        user = self.model(
            username = username,
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, password=None):

        if password is None:
            raise TypeError('Users must have a password') 
        

        user = self.create_user(
            username,
            email,
            password
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save()
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(max_length=200, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }