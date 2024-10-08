from rest_framework import generics, viewsets
from .serializers import PostSerializer
from .models import CustomUser, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
