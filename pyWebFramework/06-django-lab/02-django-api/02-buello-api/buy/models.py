from django.db import models
from authentication.models import User

# Create your models here.
class Buy(models.Model):

    CATEGORY_OPTIONS = [
        ('IT_SERVICE', 'IT_SERVICE'),
        ('FOOD', 'FOOD'),
        ('APPLIANCES', 'APPLIANCES'),
        ('TRAVEL', 'TRAVEL'),
        ('OTHERS', 'OTHERS'),
    ]
    
    category = models.CharField(choices=CATEGORY_OPTIONS, max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner