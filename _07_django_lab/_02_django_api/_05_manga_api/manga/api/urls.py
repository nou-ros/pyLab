from django.urls import path

from manga.api.views import (
    MangaList, MangaCreate, MangaDetail, MangaAuthorList, MangaAuthorDetail, MangaAuthorAvatarUpdateView, MangaImageUpdateView, ReviewCreateAPIView, ReviewDetailAPIView)

urlpatterns = [
    path('mangas/', MangaList.as_view(), name='manga_list'),
    path('mangas/<int:pk>/', MangaDetail.as_view(), name='manga_detail'),
    path('mangas/<int:pk>/image/', MangaImageUpdateView.as_view(),
         name='manga_image_update'),
    path('mangas/<int:manga_pk>/review/',
         ReviewCreateAPIView.as_view(), name="manga_review"),
    path('review/<int:pk>/', ReviewDetailAPIView.as_view(), name="review_detail"),
    path('author/', MangaAuthorList.as_view(), name='author_list'),
    path('author/<int:pk>', MangaAuthorDetail.as_view(), name="author_detail"),
    path('author/<int:author_pk>/manga/',
         MangaCreate.as_view(), name='manga_create'),
    path('author/<int:pk>/avatar/',
         MangaAuthorAvatarUpdateView.as_view(), name="avatar_update"),

]
