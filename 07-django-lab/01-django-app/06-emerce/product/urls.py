from django.urls import path 
from .views import store, product_detail, search, review

urlpatterns = [ 
    path('', store, name='store'),
    path('category/<slug:category_slug>/', store, name='products_by_category'), 
    path('category/<slug:category_slug>/product/<slug:product_slug>/', product_detail, name='product_detail'), 
    path('search/', search, name='search'), 
    path('review/<int:product_id>/',review, name="review")
]