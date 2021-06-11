from django.db import models
from rest_framework import serializers
from .models import Sell

class SellSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sell
        fields = ['service', 'amount', 'description', 'created_at', 'update_at']