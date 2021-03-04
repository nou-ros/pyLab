from django.contrib import admin

from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    # admin display list
    list_display = ('title','price', 'species', 'is_publish', 'updated_date', 'farmer')

    # list item link
    list_display_links = ('title','farmer')

    #list filter 
    list_filter = ('farmer',)

    #active item
    list_editable = ('is_publish',)

    #searching
    search_fields = ('title', 'price', 'description', 'farmer__name')

    #pagination
    list_per_page = 25
    
admin.site.register(Listing, ListingAdmin)