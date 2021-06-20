from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class MangaAuthor(models.Model):
    name = models.CharField(max_length=100)
    penname = models.CharField(max_length=100)
    country = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar = models.ImageField(upload_to="writter/", null=True, blank=True)

    def __str__(self):
        return self.name


class Mangas(models.Model):
    author = models.ForeignKey(
        MangaAuthor, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    chapter = models.IntegerField(default=1)
    publication_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to="mangaPicture/", null=True, blank=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    review_author = models.CharField(max_length=8, blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1),
                                                     MaxValueValidator(5)])

    manga = models.ForeignKey(
        Mangas, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return str(self.rating)
