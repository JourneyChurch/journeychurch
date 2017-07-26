from django import template
from django.shortcuts import get_object_or_404
from pages.models import Content

register = template.Library()

# Three Column Section:
# Custom Tag that can be accessed by {% three_column %}. Creates fields for a three column type section
@register.inclusion_tag("pages/sections/three_column.html")
def three_column(section):

    context = {
        "title": section.display_title,
        "slug": section.slug,
        "background_image": section.background_image,
        "background_color": section.background_color,
        "title_left": section.title_left,
        "content_left": section.content_left,
        "image_left": section.image_left,
        "title_center": section.title_center,
        "content_center": section.content_center,
        "image_center": section.image_center,
        "title_right": section.title_left,
        "content_right": section.content_left,
        "image_right": section.image_left,
        "center_text": section.center_text
    }

    return context
