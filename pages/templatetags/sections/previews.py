from django import template
from pages.models import PreviewGroup

register = template.Library()

# Previews Section:
# Custom Tag that can be accessed by {% previews %}. Creates fields for an previews type section
@register.inclusion_tag("pages/sections/previews.html")
def previews(section):

    # Get preview group
    try:
        preview_group = PreviewGroup.objects.get(id=section.preview_group.id)
    except PreviewGroup.DoesNotExist:
        preview_group = None

    # If preview group exists, get previews
    if preview_group:
        previews = preview_group.preview_set.all().order_by("order")
    else:
        previews = None

    # If display title
    if section.display_title:
        title = section.display_title
    else:
        title = section.title


    context = {
        "title": title,
        "slug": section.slug,
        "background_image": section.background_image,
        "background_color": section.background_color,
        "previews": previews,
    }

    return context
