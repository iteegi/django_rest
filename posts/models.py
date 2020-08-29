"""Models for Posts app."""

from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    """Posts model."""

    title = models.CharField(max_length=100)
    url = models.URLField()
    poster = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Additional settings for the Posts model."""

        orderin = ['-created']
