from django.db import models
from farmers.models import Farmer

# Create your models here.
class Listing(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    species = models.CharField(max_length=200)
    plants = models.IntegerField(default=1)
    fertilizer = models.FloatField()
    soil = models.DecimalField(max_digits=2, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_publish = models.BooleanField(default=True)

    def __str__(self):
        return self.title