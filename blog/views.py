from rest_framework import generics
from .serializers import PostSerializer
from .models import CustomUser, Post


class PostAPIListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
