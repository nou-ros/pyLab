from django.urls import path 
from .views import SellListAPIView, SellDetaiAPIView

urlpatterns = [
    path('', SellListAPIView.as_view(), name="sells"),
    path('<int:id>', SellDetaiAPIView.as_view(), name="sell"),
]