from django.db import models
from datetime import datetime 
#accessing realtors app model
from realtors.models import Realtor

# Create your models here.
class Listing(models.Model):
    # if we delete the realtor for that specific listing, the listing will not get deleted
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    # so decription will not be required
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    #not more than 2 digits, and after decimal point one number will be available
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    #as we want each photo should save as date structure
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/')
    #as these 6 images will be optional we will also include blank field. 
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    #to include current date and time
    list_date = models.DateTimeField(default=datetime.now, blank=True)


    def __str__(self):
        return self.title