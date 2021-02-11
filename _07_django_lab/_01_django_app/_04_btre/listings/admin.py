from django.contrib import admin
from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    #displaying items in listing admin
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')

    #displaying the links 
    list_display_links = ('id', 'title')

    #filter by realtors
    list_filter = ('realtor',)

    list_editable = ('is_published',)

    #search 
    search_fields = ('title', 'description', 'city', 'zipcode', 'state', 'price')

    #pagination
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)