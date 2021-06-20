from django.contrib import admin

# Register your models here.
from ebooks.models import Ebook, Review

admin.site.register(Ebook)
admin.site.register(Review)
