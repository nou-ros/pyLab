from django.urls import path 
from .views import BuyListAPIView, BuyDetaiAPIView

urlpatterns = [
    path('', BuyListAPIView.as_view(), name="buys"),
    path('<int:id>', BuyDetaiAPIView.as_view(), name="buy"),
]