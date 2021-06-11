from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Buy
# Create your views here.
from .serializers import BuySerializer 
from rest_framework import permissions

from .permissions import IsOwner
from rest_framework.parsers import FormParser, MultiPartParser

class BuyListAPIView(ListCreateAPIView):
    serializer_class = BuySerializer
    queryset = Buy.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)

class BuyDetaiAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = BuySerializer
    queryset = Buy.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner)
    lookup_field = "id"

    
    def get_queryset(self):
        return self.queryset.filter(owner=self.request.user)