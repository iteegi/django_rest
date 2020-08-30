"""Serializers for Posts models."""

from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts models."""

    class Meta:
        """Additional settings for the PostSerializer class."""

        model = Post
        fields = ['id',
                  'title',
                  'url',
                  'poster',
                  'created',
                  ]
