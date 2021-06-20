from django.db import models
from datetime import datetime

# Create your models here.
class Farmer(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to="farmers/%Y/%m/%d/")
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    seller_month = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default= datetime.now, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name