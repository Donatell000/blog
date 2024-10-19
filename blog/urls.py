from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import PostAPIList, PostAPIDestroy,\
    ProfileAPIList, ProfileAPIDetail, PostAPIListUsername, CommentAPIList, CommentAPIDetail, CommentAPIDetailComm
from django.contrib import admin

# router = routers.SimpleRouter()
# router.register(r'posts', PostViewSet)
#

urlpatterns = [
    # path('', include(router.urls)),
    path('api/posts/', PostAPIList.as_view()),
    path('api/posts/<str:username>/', PostAPIListUsername.as_view()),
    path('api/postsdelete/<int:pk>/', PostAPIDestroy.as_view()),
    path('api/profile/', ProfileAPIList.as_view()),
    path('api/profile/<str:user__username>/', ProfileAPIDetail.as_view()),
    path('api/comments/', CommentAPIList.as_view()),
    path('api/comments_id/<int:pk>/', CommentAPIDetailComm.as_view()),
    path('api/comments_post/<int:post_id>/', CommentAPIDetail.as_view()),
]
