from django.shortcuts import render

from rest_framework import generics

from .serializers import *

from .models import *

# Create your views here.

class MyAPIView(generics.ListAPIView):

    queryset = Africa.objects.all()

    serializer_class = Myserializer
