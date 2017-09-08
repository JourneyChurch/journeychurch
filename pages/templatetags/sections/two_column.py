from django import template
from django.shortcuts import get_object_or_404
from pages.models import Content

register = template.Library()

# Two Column Section:
# Custom Tag that can be accessed by {% two_column %}. Creates fields for a two column type section
@register.inclusion_tag("pages/sections/two_column.html")
def two_column(section):

    context = {
        "title": section.display_title,
        "slug": section.slug,
        "background_image": section.background_image,
        "background_color": section.background_color,
        "title_left": section.title_left,
        "content_left": section.content_left,
        "image_left": section.image_left,
        "title_right": section.title_right,
        "content_right": section.content_right,
        "image_right": section.image_right,
        "center_text": section.center_text
    }

    return context
