from django.urls import path, include
#to work with API viewset
from rest_framework.routers import DefaultRouter

from profile_app import views

#work with APIViewset
router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
#work with ModelViewSet
router.register('profile', views.UserProfileViewSet)
#prfileFeed 
router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
   #work with APIView
   path('hello-view/', views.HelloApiView.as_view()),
   path('', include(router.urls)),
   path('login/', views.UserLoginApiView.as_view())
]