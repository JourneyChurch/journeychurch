from django.db import models
from entries.models import Entry

# Tinymce: wysiwyg editor for django admin
# https://github.com/aljosa/django-tinymce
from tinymce.models import HTMLField


class VideoGroup(Entry):
    """
    A group of video entries
    """

    # Display title of video group
    display_title = models.CharField(max_length=100, null=True)


class Video(Entry):
    """
    A video entry
    """

    # Displayed title of video
    display_title = models.CharField(max_length=100, null=True)

    # Description of video
    description = HTMLField(max_length=60000, blank=True, null=True)

    # Youtube ID for video
    youtube_id = models.CharField(max_length=11, null=True)

    # Video Groups
    video_groups = models.ManyToManyField(VideoGroup, blank=True)
