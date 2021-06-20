from django.db import models
from authentication.models import User

# Create your models here.
class Sell(models.Model):

    SERVICE_OPTIONS = [
        ('WEB_DEVELOPMENT', 'WEB_DEVELOPMENT'),
        ('ANDROID', 'ANDROID'),
        ('IOS', 'IOS'),
        ('MACHINE_LEARNING', 'MACHINE_LEARNING'),
        ('OTHERS', 'OTHERS'),
    ]
    
    service = models.CharField(choices=SERVICE_OPTIONS, max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

        
    def __str__(self):
        return str(self.owner)