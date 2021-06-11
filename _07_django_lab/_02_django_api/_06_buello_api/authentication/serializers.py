from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import ModelSerializer
from .models import User
from django.contrib import auth

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