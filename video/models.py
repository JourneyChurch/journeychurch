from django.db import models

# Tinymce: wysiwyg editor for django admin
# https://github.com/aljosa/django-tinymce
from tinymce.models import HTMLField


class VideoGroup(models.Model):
    """
    A group of video entries
    """

    # Title of Video Group
    title = models.CharField(max_length=100, unique=True)

    # Display title of video group
    display_title = models.CharField(max_length=100)

    # Slug for video group based on title
    slug = models.SlugField(max_length=200, unique=True)

    # Representation in admin
    def __str__(self):
        return self.title


class Video(models.Model):
    """
    A video entry
    """

    # Title of Video
    title = models.CharField(max_length=100, unique=True)

    # Displayed title of video
    display_title = models.CharField(max_length=100)

    # Slug based off of title
    slug = models.SlugField(max_length=200, unique=True)

    # Description of video
    description = HTMLField(max_length=60000, blank=True, null=True)

    # Youtube ID for video
    youtube_id = models.CharField(max_length=11)

    # Video Groups
    video_groups = models.ManyToManyField(VideoGroup)

    # Representation in admin
    def __str__(self):
        return self.title
