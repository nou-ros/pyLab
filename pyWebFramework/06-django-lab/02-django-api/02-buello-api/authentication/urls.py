from django.urls import path 
from .views import RegisterView, VerifyEmail, LoginAPIView, PasswordResetAPIView, PasswordTokenCheckAPIView, SetNewPasswordAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('register', RegisterView.as_view(), name="register"),
    path('verify/', VerifyEmail.as_view(), name='verify'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('request-reset-password/',PasswordResetAPIView.as_view(), name='request-reset-password'),
    path('reset-password-check/<uidb64>/<token>/', PasswordTokenCheckAPIView.as_view(), name="reset-password-check"),

    path('password-reset-complete', SetNewPasswordAPIView.as_view(), name="password-reset-complete")
]