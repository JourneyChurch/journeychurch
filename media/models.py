from django.db import models
from entries.models import Entry
from profiles.models import Profile

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

    # Video image
    image = models.ImageField(upload_to="video/", max_length=200, blank=True, null=True)

    # Video Groups
    video_groups = models.ManyToManyField(VideoGroup, blank=True)


class Series(Entry):
    """
    Series for experiences
    """

    # Type of series
    SERIES_TYPES = (
        ('weekend', 'Weekend'),
        ('college', 'College'),
    )
    series_type = models.CharField(max_length=7, choices=SERIES_TYPES, default='weekend')

    # Series image
    image = models.ImageField(upload_to="series/", max_length=200)


class Experience(Entry):
    """
    On Demand experience
    """

    # Video
    video = models.ForeignKey(Video, on_delete=models.CASCADE, null=True)

    # Series that experience belongs to
    series = models.ForeignKey(Series, on_delete=models.CASCADE, null=True)

    # Profile of speaker
    speaker = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)

    # Notes
    notes = HTMLField(max_length=60000, blank=True, null=True)

    # Simplecast audio podcast id
    simplecast_id = models.CharField(max_length=8, blank=True, null=True)
