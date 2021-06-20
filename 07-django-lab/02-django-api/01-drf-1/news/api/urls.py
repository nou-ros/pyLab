#api endpoint
from django.urls import path    
# from news.api.views import article_list_create_api_view, article_detail_api_view

# urlpatterns = [
#     path("articles/", article_list_create_api_view, name="article_create_list"),
#     path("articles/<int:pk>/", article_detail_api_view, name="article_detail")
# ]

from news.api.views import (ArticleListCreaetAPIView, 
            ArticleDetailApiView, JournalistListCreateAPIView)

urlpatterns = [
    path("articles/", ArticleListCreaetAPIView.as_view(), name="article_create_list"),
    path("articles/<int:pk>/", ArticleDetailApiView.as_view(), name="article_detail"),
    path("journalists/", JournalistListCreateAPIView.as_view(), name="jurnalist_lsit")
]