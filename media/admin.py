from django.contrib import admin
from media.models import VideoGroup, Video, Series, Experience
from entries.admin import EntryAdmin


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


class SeriesAdmin(EntryAdmin):
    """
    Manages admin for series
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Series Fields', {
            'fields': ('series_type', 'image')
        },)
    )

    # Show all objects in admin
    def get_queryset(self, request):
         return Series.all_objects.get_queryset()


class ExperienceAdmin(EntryAdmin):
    """
    Manages admin for experiences
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Experience Fields', {
            'fields': ('video', 'series', 'speaker', 'notes', 'simplecast_id')
        },)
    )

    # Show all objects in admin
    def get_queryset(self, request):
         return Experience.all_objects.get_queryset()


admin.site.register(VideoGroup, VideoGroupAdmin)
admin.site.register(Video, VideoAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Experience, ExperienceAdmin)
