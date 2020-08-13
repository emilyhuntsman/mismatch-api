from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics
from .models import Card
from .serializers import CardSerializer

class CardList(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
