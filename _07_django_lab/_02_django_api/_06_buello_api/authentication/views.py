from .serializers import RegisterSerializer, EmailVerificationSerializer, LoginSerializer
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