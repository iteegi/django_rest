"""Views for Posts app."""

from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListCreateAPIView):
    """View for a list of all posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        """Override save behavior.

        Called by CreateModelMixin.
        """
        serializer.save(poster=self.request.user)
