from django.db import models


class Social(models.Model):
    """
    Social links that go with another resource
    """

    # Title of social media
    title = models.CharField(max_length=100, unique=True)

    # Facebook
    facebook = models.CharField(max_length=2000, blank=True, null=True)

    # Twitter
    twitter = models.CharField(max_length=2000, blank=True, null=True)

    # Instagram
    instagram = models.CharField(max_length=2000, blank=True, null=True)

    # Youtube
    youtube = models.CharField(max_length=2000, blank=True, null=True)

    # Snapchat
    snapchat = models.CharField(max_length=2000, blank=True, null=True)

    def __str__(self):
        return self.title
