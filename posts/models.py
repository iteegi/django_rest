"""Models for Posts app."""

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """Post model."""

    title = models.CharField(max_length=100)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Additional settings for the Posts model."""

        ordering = ['-created']


class Vote(models.Model):
    """Model for voices."""

    voter = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
