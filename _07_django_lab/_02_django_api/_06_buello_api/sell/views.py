from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Sell
# Create your views here.
from .serializers import SellSerializer 
from rest_framework import permissions

from buy.permissions import IsOwner


class SellListAPIView(ListCreateAPIView):
    serializer_class = SellSerializer
    queryset = Sell.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class SellDetaiAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SellSerializer
    queryset = Sell.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = "id"

    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)