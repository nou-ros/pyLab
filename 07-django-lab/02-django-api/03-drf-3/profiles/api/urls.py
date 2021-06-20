from django.urls import path, include

from profiles.api.views import ProfileViewSet, ProfileStatusViewSet, AvatarUpdateView

from rest_framework.routers import DefaultRouter

# with router viewsets
router = DefaultRouter()
router.register(r'profiles', ProfileViewSet)
# when filtering by name
router.register(r'status', ProfileStatusViewSet, basename="status")
# router.register(r'status', ProfileStatusViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('avatar/', AvatarUpdateView.as_view(), name="avatar_update")
]

'''
# without router viewsets
profile_list = ProfileViewSet.as_view({"get": "list"})
profile_detail = ProfileViewSet.as_view({"get": "retrieve"})

urlpatterns = [
    path('profiles/', profile_list, name='profile-list'),
    path('profiles/<int:pk>/', profile_detail, name='profile-detail'),
]
'''
'''
from profiles.api.views import ProfileList

urlpatterns = [
    path('profiles/', ProfileList.as_view(), name='profile-list')
]
'''
