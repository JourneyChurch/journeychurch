from django.contrib import admin
from video.models import VideoGroup, Video


class VideoGroupAdmin(admin.ModelAdmin):
    """
    Admin for video groups
    """
    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}


class VideoAdmin(admin.ModelAdmin):
    """
    Admin for videos
    """
    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(VideoGroup, VideoGroupAdmin)
admin.site.register(Video, VideoAdmin)
