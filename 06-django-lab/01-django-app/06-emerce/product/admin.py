from django.contrib import admin

# Register your models here.
from .models import Product, Variation, ReviewRating, ProductGallery


import admin_thumbnails

@admin_thumbnails.thumbnail('image') # model field name
class ProductGalleryAdmin(admin.TabularInline):
    model = ProductGallery
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'stock', 'category', 'modified_date', 'created_date', 'is_available')
    prepopulated_fields = {"slug": ("product_name", )}
    inlines = [ProductGalleryAdmin]


class VariationAdmin(admin.ModelAdmin):
    list_display = ('product', 'variation_category', 'variation_value', 'is_active', 'created_date', 'modified_date')
    list_editable = ('is_active', )
    list_filter = ('product__category', 'variation_category', 'variation_value')



admin.site.register(Product, ProductAdmin)
admin.site.register(Variation, VariationAdmin)
admin.site.register(ReviewRating)
admin.site.register(ProductGallery)