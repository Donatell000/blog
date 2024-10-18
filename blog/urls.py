from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import PostAPIList, PostAPIUpdate, PostAPIDestroy, ProfileAPIList, ProfileAPIDetail
from django.contrib import admin

# router = routers.SimpleRouter()
# router.register(r'posts', PostViewSet)
#

urlpatterns = [
    # path('', include(router.urls)),
    path('api/posts/', PostAPIList.as_view()),
    path('api/posts/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/postsdelete/<int:pk>/', PostAPIDestroy.as_view()),
    path('api/profile/', ProfileAPIList.as_view()),
    path('api/profile/<int:user_id>/', ProfileAPIDetail.as_view()),

]
