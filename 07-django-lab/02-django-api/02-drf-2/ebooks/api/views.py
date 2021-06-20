from rest_framework import generics
from rest_framework import mixins

from ebooks.models import Ebook, Review
from ebooks.api.serializers import ReviewSerializer, EbookSerializer

from rest_framework.generics import get_object_or_404

from rest_framework import permissions

from ebooks.api.permissions import IsAdminUserOrReadOnly

from ebooks.api.pagination import SmallSetPagination

# concreate view class approach
class EbookListCreateAPIView(generics.ListCreateAPIView):
    # when we use pagination it is better to use a ordering 
    queryset = Ebook.objects.all().order_by("-id")
    serializer_class = EbookSerializer
    # providing view seperate permissions
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # view specific pagination
    pagination_class = SmallSetPagination

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # connecting the specific ebook with the review - foreign_key operation
    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get('ebook_pk')
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        serializer.save(ebook=ebook)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

'''
# generics api view approach
class EbookListCreateAPIView(generics.GenericAPIView, 
                            mixins.ListModelMixin, 
                            mixins.CreateModelMixin):
    
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
'''