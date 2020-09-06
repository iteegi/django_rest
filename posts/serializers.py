"""Serializers for Posts models."""

from rest_framework import serializers
from .models import Post, Vote


class PostSerializer(serializers.ModelSerializer):
    """Serializer for posts models."""

    poster = serializers.ReadOnlyField(source='poster.username')
    poster_id = serializers.ReadOnlyField(source='poster.id')

    class Meta:
        """Additional settings for the PostSerializer class."""

        model = Post
        fields = ['id',
                  'title',
                  'url',
                  'poster',
                  'poster_id',
                  'created',
                  ]


class VoteSerializer(serializers.ModelSerializer):
    """Serializer for votes models."""

    class Meta:
        """Additional settings for the VoteSerializer class."""

        model = Vote
        fields = ['id',
                  ]
