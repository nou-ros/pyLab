from rest_framework import generics
from rest_framework import mixins

from rest_framework.generics import get_object_or_404

from ebooks.models import Ebook, Review
from ebooks.api.serializers import EbookSerializer, ReviewSerialzier

# for specific permission
from rest_framework import permissions

from ebooks.api.permissions import IsAdminUserOrReadOnly, IsReviewAuthorOrReadOnly

from rest_framework.exceptions import ValidationError

# work with concrete view class (2nd approach) we will not need the mixins as they are already pre build in ListCreateAPIView
class EbookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    # providing permissions seprately
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EbookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer
    # providing permissions seprately
    permission_classes = [IsAdminUserOrReadOnly]

class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialzier

    # connecting ebook instance
    def perform_create(self, serializer):
        ebook_pk = self.kwargs.get("ebook_pk")
        ebook = get_object_or_404(Ebook, pk=ebook_pk)
        permission_classes = [permissions.IsAuthenticatedOrReadOnly]

        # 
        review_author = self.request.user

        # validation check for if a review from a user already exists not post again
        review_queryset = Review.objects.filter(ebook=ebook, review_author=review_author)

        if review_queryset.exists:
            raise ValidationError("You have already reviewed this book.")

        serializer.save(ebook=ebook, review_author=review_author)

class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerialzier

    permission_classes = [IsReviewAuthorOrReadOnly]
    
# work with generic api view and mixins (first approach)
'''
class EbookListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):

    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
'''