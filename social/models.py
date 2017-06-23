from django.db import models
from entries.models import Entry

class Social(Entry):
    """
    Social links that go with another resource
    """

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
