from django.db import models

# Create your models here.


class Director(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)

    def __str__(self):
        return self.name + ' ' + self.surname

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.IntegerField(default=2000)
    director = models.ForeignKey(Director, on_delete=models.PROTECT, null=True, blank=True)

    def __str__(self):
        return self.title

def sub(a,b):
    return a-b