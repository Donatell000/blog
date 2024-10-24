from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import PostViewSet, ProfileViewSet
from django.contrib import admin

router = routers.SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('api/comments/', CommentAPIList.as_view()),
    # path('api/comments_id/<int:pk>/', CommentAPIDetailComm.as_view()),
    # path('api/comments_post/<int:post_id>/', CommentAPIDetail.as_view()),
]
