from django.contrib import admin
from entries.admin import EntryAdmin
from video.models import VideoGroup, Video

class VideoGroupAdmin(EntryAdmin):
    """
    Manages admin for video groups
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Video Group Fields', {
            'fields': ('display_title',)
        },)
    )

class VideoAdmin(EntryAdmin):
    """
    Manages admin for videos
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Video Fields', {
            'fields': ('display_title', 'description', 'youtube_id', 'video_groups',)
        },)
    )

admin.site.register(VideoGroup, VideoGroupAdmin)
admin.site.register(Video, VideoAdmin)
