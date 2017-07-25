from django import template
from django.shortcuts import get_object_or_404
from pages.models import Content

register = template.Library()

# Default Section:
# Custom Tag that can be accessed by {{ video_group }}. Creates fields for a default type section
@register.inclusion_tag("pages/sections/video.html")
def video_group(section):

    first_video = section.video_group.video_set.order_by('-entry_date').first()

    context = {
        "title": section.display_title,
        "slug": section.slug,
        "background_image": section.background_image,
        "background_color": section.background_color,
        "video_title": first_video.display_title,
        "video_description": first_video.description,
        "youtube_id": first_video.youtube_id
    }

    return context
