from django.urls import path
from .views import CustomUserApiView
from .views import message_welcome

urlpatterns = [
    path('', message_welcome),
    path('userlist/', CustomUserApiView.as_view())
]
