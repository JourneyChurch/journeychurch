from django import template
from django.shortcuts import get_object_or_404
from pages.models import Content
from video.models import VideoGroup

register = template.Library()

# Default Section:
# Custom Tag that can be accessed by {% video_group %}. Creates fields for a default type section
@register.inclusion_tag("pages/sections/video.html")
def video_group(section):

    first_video = None

    # Make sure video group exists and is public
    try:
        video_group = VideoGroup.objects.get(id=section.video_group.id)
    except VideoGroup.DoesNotExist:
        video_group = None

    # If video group is public try to get first video
    if video_group != None:
        first_video = video_group.video_set.order_by('-entry_date').first()

        if first_video:
            video_title = first_video.display_title
            video_description = first_video.description
            youtube_id = first_video.youtube_id
        else:
            video_title = None
            video_description = None
            youtube_id = None

    # If video group is not public, leave blank
    else:
        video_title = None
        video_description = None
        youtube_id = None

    context = {
        "title": section.display_title,
        "slug": section.slug,
        "background_image": section.background_image,
        "background_color": section.background_color,
        "video": first_video,
        "video_title": video_title,
        "video_description": video_description,
        "youtube_id": youtube_id
    }

    return context
