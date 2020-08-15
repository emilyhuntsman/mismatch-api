from rest_framework import serializers
from .models import Card
from django.contrib.auth.models import User
from djoser.serializers import TokenSerializer
from djoser.conf import settings as djoser_settings
from stream_chat import StreamChat
from django.conf import settings

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

class StreamTokenSerializer(TokenSerializer):
    stream_token = serializers.SerializerMethodField()

    class Meta:
        model = djoser_settings.TOKEN_MODEL
        fields = ('auth_token','stream_token')

    def get_stream_token(self,obj):
        client = StreamChat(api_key=settings.STREAM_API_KEY, api_secret=settings.STREAM_API_SECRET)
        token = client.create_token(obj.user.id)
        return token
