from django.db import models

# 1st-> to work with django User model we used AbstractBaseUser, and to provide certain permission we used PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

#3-> teach django how to use our new user model
from django.contrib.auth.models import BaseUserManager

#to retrive settings file
from django.conf import settings

class UserProfileManager(BaseUserManager):
    """4-> Helps django to work with our custom model"""
    def create_user(self, email, name, password=None):
        """Creates a new user profile object."""

        if not email:
            raise ValueError('Users must have an email address.')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, email, name, password):
        """create and saves a new superuser with given details. """

        user= self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self.db)

        return user
    

# Create your models here.
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """2-> Represents a user profile inside our system"""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    
    """ to help manage the UserProfiles. It is required to create custom user model."""    
    objects = UserProfileManager()

    """with this anyone will be able to login with email instead of username"""
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    """helper functions"""

    def get_fullname(self):
        """Used to get a users full name."""
        return self.name

    def get_shortname(self):
        """Used to get a users short name"""
        return self.name

    def __str__(self):
        return self.email



class ProfileFeedItem(models.Model):
    """Profile status update"""
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete= models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""
        return self.status_text