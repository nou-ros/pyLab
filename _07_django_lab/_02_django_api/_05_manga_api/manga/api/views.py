from rest_framework import generics
from manga.models import MangaAuthor, Mangas, Review
from manga.api.serializers import (
    MangaSerializer, MangaAuthorSerializer,
    MangaAuthorAvatarSerializer, MangaImageSerializer, ReviewSerializer)

from rest_framework.generics import get_object_or_404

from manga.api.pagination import SmallSetPagination

from rest_framework import mixins


class MangaAuthorList(generics.ListCreateAPIView):
    queryset = MangaAuthor.objects.all()
    serializer_class = MangaAuthorSerializer
    pagination_class = SmallSetPagination


class MangaAuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MangaAuthor.objects.all()
    serializer_class = MangaAuthorSerializer


class MangaAuthorAvatarUpdateView(generics.UpdateAPIView):
    queryset = MangaAuthor.objects.all()
    serializer_class = MangaAuthorAvatarSerializer


class MangaList(generics.ListAPIView):
    queryset = Mangas.objects.all().order_by("-id")
    serializer_class = MangaSerializer
    pagination_class = SmallSetPagination


class MangaCreate(generics.CreateAPIView):
    queryset = Mangas.objects.all()
    serializer_class = MangaSerializer

    def perform_create(self, serializer):
        author_pk = self.kwargs.get('author_pk')
        author = get_object_or_404(MangaAuthor, pk=author_pk)
        serializer.save(author=author)


class MangaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mangas.objects.all()
    serializer_class = MangaSerializer


class MangaImageUpdateView(generics.UpdateAPIView):
    queryset = Mangas.objects.all()
    serializer_class = MangaImageSerializer


class ReviewCreateAPIView(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # connecting the specific manga review - foreign_key operation
    def perform_create(self, serializer):
        manga_pk = self.kwargs.get('manga_pk')
        manga = get_object_or_404(Mangas, pk=manga_pk)
        serializer.save(manga=manga)


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
