from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib import auth


from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

class RegisterSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=4, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    
    def validate(self, attrs):
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('The username should only contain alphanumeric value')

        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    

class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField()

    class Meta:
        model = User
        fields = ['token']


class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    password = serializers.CharField(min_length=4, write_only=True)
    username = serializers.CharField(read_only=True)
    tokens = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ['email', 'password', 'username', 'tokens']
    
    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')

        user = auth.authenticate(email=email, password=password)

        # import pdb
        # pdb.set_trace()

        if not user:
            raise AuthenticationFailed('Invalid credentials')
        if not user.is_active:
            raise AuthenticationFailed('Account disabled, contact admin')
        if not user.is_verified:
            raise AuthenticationFailed('Email was not verified')
        
        
        return {
            'email': user.email, 
            'username': user.username,
            'tokens': user.tokens
        }

class ResetPasswordSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ['email']
    

class SetNewPassworSerializer(serializers.ModelSerializer):

    password = serializers.CharField(min_length=4, write_only=True)
    token = serializers.CharField(write_only=True)
    uidb64 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['password', 'token', 'uidb64']
    
    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            
            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed("The reset link is invalid", 401)

            user.set_password(password)
            user.save()

            return (user)

        except Exception as e:
            raise AuthenticationFailed('The reset link is invlaid', 401)
        
        
        return super().validate(attrs)
