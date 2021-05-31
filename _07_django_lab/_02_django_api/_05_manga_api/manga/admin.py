from django.contrib import admin

# Register your models here.
from .models import MangaAuthor, Mangas, Review

admin.site.register(Mangas)
admin.site.register(MangaAuthor)
admin.site.register(Review)
