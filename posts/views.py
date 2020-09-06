"""Views for Posts app."""

from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError

from .models import Post, Vote
from .serializers import PostSerializer, VoteSerializer


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


class VoteCreate(generics.CreateAPIView):
    """View to vote for a specific post."""

    queryset = Post.objects.all()
    serializer_class = VoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Override the initial queryset."""
        user = self.request.user
        post = Post.objects.get(pk=self.kwargs['pk'])
        return Vote.objects.filter(voter=user, post=post)

    def perform_create(self, serializer):
        """Override save behavior.

        Called by CreateModelMixin.
        """
        if self.get_queryset().exists():
            raise ValidationError('You have already voted for this post!')
        serializer.save(voter=self.request.user,
                        post=Post.objects.get(pk=self.kwargs['pk']))
