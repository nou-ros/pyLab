from django.db import models

from django.utils import timezone

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField(default=True)
    slug = models.SlugField(max_length=100)
    categories = models.ManyToManyField('blog.Category')
    # this will raise an issue to call the Category model above Blog model so we took the previous approach
    # categories = models.ManyToManyField(Category) 
    def __str__(self):
        return self.title

    #number of days since a post created
    @property
    def days_since_creation(self):
        diff = timezone.now() - self.date_created

        return diff.days


class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta: 
        verbose_name_plural = 'Categories'

