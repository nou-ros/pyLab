from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must need an email')
        if not username:
            raise ValueError('User should have a username')

        user = self.model(
            email = self.normalize_email(email), 
            username=username, 
            first_name=first_name, 
            last_name=last_name
            )
        
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):

        user = self.create_user(
            email = email, 
            username=username, 
            first_name=first_name, 
            last_name=last_name, 
            password=password
        )
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True

        user.save()
        return user


# user model
class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=100)

    # required
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    # login with email
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    objects = MyAccountManager()

    def __str__(self):
        return self.email

    
    def has_perm(self, perm, obj=None):
        return self.is_superuser
    
    def has_module_perms(self, add_label):
        return True

    def full_name(self):
        return f'{self.first_name}  {self.last_name}'

class UserProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    address_line_1 = models.CharField(blank=True, max_length=255)
    address_line_2 = models.CharField(blank=True, max_length=255)
    profile_picture = models.ImageField(blank=True, upload_to='userprofile/')
    city = models.CharField(blank=True, max_length=50)
    state = models.CharField(blank=True, max_length=50)
    country = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.user.email

    def full_address(self):
        return f'{self.address_line_1} {self.address_line_2}' 
