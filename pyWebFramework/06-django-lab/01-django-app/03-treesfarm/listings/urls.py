from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='listing'),
    path('<int:listing_id>', views.details, name='details'),
    path('search', views.search, name='search'),
]