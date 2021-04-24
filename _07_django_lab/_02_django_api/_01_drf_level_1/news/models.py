from django.db import models

class Journalist(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    biography = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

# Create your models here.
class Article(models.Model):
    # we build it to check nested relationship
    author = models.ForeignKey(Journalist, models.CASCADE, related_name="articles")
    # author = models.CharField(max_length=50)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    body = models.TextField()
    location = models.CharField(max_length=200)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} - {self.title}"