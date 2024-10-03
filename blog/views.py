from rest_framework import generics
from .serializers import CustomUserSerializer, PostSerializer
from .models import CustomUser, Post


class CustomUserAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
