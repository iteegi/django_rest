"""Views for Posts app."""

from rest_framework import generics

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """View for a list of all posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Override save behavior."""
        serializer.save(poster=self.request.user)
