"""Serializers for Posts models."""

from rest_framework import serializers
from .post import Posts


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts models."""

    class Meta:
        """Additional settings for the PostSerializer class."""

        model = Posts
        fields = ['id',
                  'title',
                  'url',
                  'poster',
                  'created',
                  ]
