from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import PostAPIList, PostAPIUpdate, PostAPIDestroy, ProfileAPIList, ProfileAPIDetail, PostAPIListUsername
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

]
