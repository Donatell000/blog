from django.urls import path, include
from django.contrib import admin
from rest_framework import routers
from .views import PostAPIList, PostAPIUpdate, PostAPIDestroy
from django.contrib import admin

# router = routers.SimpleRouter()
# router.register(r'posts', PostViewSet)
#

urlpatterns = [
    # path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/posts/', PostAPIList.as_view()),
    path('api/posts/<int:pk>/', PostAPIUpdate.as_view()),
    path('api/postsdelete/<int:pk>/', PostAPIDestroy.as_view()),

]
