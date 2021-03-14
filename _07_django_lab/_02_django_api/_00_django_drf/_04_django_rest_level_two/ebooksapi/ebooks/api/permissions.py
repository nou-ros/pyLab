from rest_framework import permissions

# creating custom permission with IsAdminUserOrReadOnly
class IsAdminUserOrReadOnly(permissions.IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super().has_permission(request, view)
        return request.method is permissions.SAFE_METHODS or is_admin


# for editing a review
class IsReviewAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.review_author == request.user
