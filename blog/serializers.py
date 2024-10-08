from rest_framework import serializers
from .models import CustomUser, Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'  # ('title', 'content', 'author')
