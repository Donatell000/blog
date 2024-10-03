from django.http import HttpResponse
from rest_framework import generics
from .serializers import CustomUserSerializer
from .models import CustomUser, Post


def message_welcome(request):
    return HttpResponse("Делитесь своими мыслями!")


class CustomUserApiView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
