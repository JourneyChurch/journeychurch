from django import template
from django.shortcuts import get_object_or_404
from pages.models import Content
from media.models import Video

register = template.Library()

# Default Section:
# Custom Tag that can be accessed by {% video %}. Creates fields for a default type section
@register.inclusion_tag("pages/sections/video.html")
def video(section):

    # Assume these are empty at first
    video_title = None
    video_description = None
    video_youtube_id = None

    # Check if section video exists and is public
    try:
        video = Video.objects.get(id=section.video.id)
    except Video.DoesNotExist:
        video = None

    # If video exists and is public
    if video != None:
        video_title = video.display_title
        video_description = video.description
        video_youtube_id = video.youtube_id

    context = {
        "title": section.display_title,
        "slug": section.slug,
        "background_image": section.background_image,
        "background_color": section.background_color,
        "video_title": video_title,
        "video_description": video_description,
        "youtube_id": video_youtube_id
    }

    return context
