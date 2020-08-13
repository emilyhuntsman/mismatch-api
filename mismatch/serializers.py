from rest_framework import serializers
from .models import Card
from django.contrib.auth.models import User

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('q','a','b')

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
