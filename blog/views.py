from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication
from .filters import PostFilter, ProfileFilter
from .permissions import IsAuthorOnly
from .serializers import PostSerializer, ProfileSerializer, CommentSerializer
from .models import Post, Profile, Comment
from rest_framework.permissions import IsAuthenticated, AllowAny


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    authentication_classes = (JWTAuthentication,)
    filter_backends = (DjangoFilterBackend, )
    filterset_class = ProfileFilter
    http_method_names = ['get', 'put', 'patch', 'delete']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), IsAuthorOnly()]



class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (JWTAuthentication, )
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']
    filter_backends = (DjangoFilterBackend, )
    filterset_class = PostFilter

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), IsAuthorOnly()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# class CommentAPIList(generics.ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#
#
# class CommentAPIDetail(generics.ListAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     lookup_field = 'post_id'
#
#
# class CommentAPIDetailComm(generics.RetrieveUpdateAPIView):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = (IsAuthorOnly,)
#     authentication_classes = (JWTAuthentication,)
