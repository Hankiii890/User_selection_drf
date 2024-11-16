from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer


class UserDetailViews(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    