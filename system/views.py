from django.shortcuts import render
from django.http import HttpResponse, request
from rest_framework import viewsets

from .Serializers import *


# Create your views here.
class UserAPI(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
