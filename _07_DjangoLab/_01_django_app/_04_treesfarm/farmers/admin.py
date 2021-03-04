from django.contrib import admin

from .models import Farmer

# Register your models here.
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'phone', 'hire_date', 'updated_date')

    list_display_links = ('name', 'email')

    search_fields = ('name',)

admin.site.register(Farmer, FarmerAdmin)