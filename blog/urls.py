from django.urls import path
from .views import CustomUserAPIView, PostAPIView

urlpatterns = [
    path('userlist/', CustomUserAPIView.as_view()),
    path('userlist/posts', PostAPIView.as_view()),
]
