from rest_framework import generics, viewsets
from rest_framework_simplejwt.authentication import JWTAuthentication

from .permissions import IsOwnerOrReadOnly, IsAuthorOnly
from .serializers import PostSerializer, ProfileSerializer, CommentSerializer
from .models import Post, Profile, Comment
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (JWTAuthentication, )
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAuthenticated(), IsAuthorOnly()]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# class PostAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIListUsername(generics.ListAPIView):
#     serializer_class = PostSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
#
#     def get_queryset(self):
#         username = self.kwargs['username']
#         return Post.objects.filter(user__username=username)
#
#
# class PostAPIUpdate(generics.RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsOwnerOrReadOnly,)
#
#
# class PostAPIDestroy(generics.DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = (IsAuthorOnly, )
#     authentication_classes = (JWTAuthentication,)
#
#
# class ProfileAPIList(generics.ListAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#
#
# class ProfileAPIDetail(generics.RetrieveAPIView):
#     queryset = Profile.objects.all()
#     serializer_class = ProfileSerializer
#     lookup_field = 'user__username'
#     # permission_classes = (IsAuthenticated, )
#     # authentication_classes = (JWTAuthentication,)
#
#
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
