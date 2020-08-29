"""Views for Posts app."""

from rest_framework import generics

from .models import Posts
from .serializers import PostSerializer


class PostList(generics.ListAPIView):
    """View for a list of all posts."""

    queryset = Posts.objects.all()
    serializer_class = PostSerializer
