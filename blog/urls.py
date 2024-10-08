from django.urls import path
from .views import PostAPIListView, PostAPIDetailView

urlpatterns = [
    path('posts/', PostAPIListView.as_view()),
    path('posts/<int:pk>', PostAPIDetailView.as_view()),
]
