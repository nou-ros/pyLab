from django.db import models
from rest_framework import serializers
from .models import Buy

class BuySerializer(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = ['category', 'amount', 'description', 'created_at', 'update_at']