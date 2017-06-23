from django.contrib import admin
from entries.admin import EntryAdmin
from video.models import VideoGroup, Video

admin.site.register(VideoGroup, EntryAdmin)
admin.site.register(Video, EntryAdmin)
