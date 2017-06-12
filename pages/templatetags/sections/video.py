from django import template
from django.shortcuts import get_object_or_404
from pages.models import Content

register = template.Library()

# Default Section:
# Custom Tag that can be accessed by {{ video }}. Creates fields for a default type section
@register.inclusion_tag("pages/sections/video.html")
def video(section):

    context = {
        "title": section.display_title,
        "slug": section.slug,
        "background_image": section.background_image,
        "background_color": section.background_color,
        "video_title": section.video.display_title,
        "video_description": section.video.description,
        "youtube_id": section.video.youtube_id
    }

    return context
