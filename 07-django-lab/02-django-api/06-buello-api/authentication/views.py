from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer, ResetPasswordSerializer, SetNewPassworSerializer
from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .utils import Verification
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
import jwt
from django.conf import settings

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .renderers import UserRender

from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

class RegisterView(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    renderer_classes = (UserRender,)
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('verify')
        absurl = 'http://'+current_site+relative_link+"?token="+str(token)
        email_body = 'Hello, '+user.username+" Use the link to verify your email \n" + absurl
        data = {
            'subject': 'Verify your email',
            'body': email_body, 
            'to':user.email
        }


        Verification.send_email(data)
        return Response(user_data, status=status.HTTP_201_CREATED)
        

class VerifyEmail(views.APIView):

    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING
    )

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')

        try: 
            # as token encodes with secret key
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            user = User.objects.get(id=payload['user_id'])

            if not user.is_verified:
                #making the user verified
                user.is_verified = True
                user.save()

            return Response({'email': 'Succefully activated'}, status=status.HTTP_200_OK)


        except jwt.ExpiredSignatureError:
            return Response({'error': 'Activation expired'}, status=status.HTTP_400_BAD_REQUEST)

        except jwt.exceptions.DecodeError:
            return Response({'error': 'Invalid Token'}, status=status.HTTP_400_BAD_REQUEST)


class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        login_data = serializer.data
        return Response(login_data, status=status.HTTP_200_OK)


class PasswordResetAPIView(generics.GenericAPIView):

    serializer_class = ResetPasswordSerializer
    def post(self, request):
        
        serializer = self.serializer_class(data=request.data)
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64=urlsafe_base64_encode(smart_bytes(user.id)) # encoding user id
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request).domain
            relative_link = reverse('reset-password-check', kwargs={'uidb64': uidb64, 'token': token})
            absurl = 'http://'+current_site+relative_link
            email_body = "Hello,  Use the link to reset your password \n" + absurl
            data = {
                'subject': 'Reset password',
                'body': email_body, 
                'to':user.email
            }


            Verification.send_email(data)
        return Response({'Success': "We have sent you an email to reset your password"}, status=status.HTTP_200_OK)


class PasswordTokenCheckAPIView(generics.GenericAPIView):

    def get(self, request, uidb64, token):
        
        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'Error': 'Invalid token, please request a new one.'}, status=status.HTTP_401_UNAUTHORIZED)


            return Response({'Success': True, "message": "Valid credentials", 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)
        
        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'Error': 'Invalid token, please request a new one.'}, status=status.HTTP_401_UNAUTHORIZED)


class SetNewPasswordAPIView(generics.GenericAPIView):
    serializer_class = SetNewPassworSerializer

    def patch(self, request):
        serializer = self.serializer_class(data = request.data)

        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': "Password reset successfully."}, status=status.HTTP_200_OK)