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

    # Show all objects in admin
    def get_queryset(self, request):
         return VideoGroup.all_objects.get_queryset()


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

    # Show all objects in admin
    def get_queryset(self, request):
         return Video.all_objects.get_queryset()


admin.site.register(VideoGroup, VideoGroupAdmin)
admin.site.register(Video, VideoAdmin)
