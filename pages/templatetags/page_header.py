from django import template

register = template.Library()

# Page Header:
# Custom Tag that can be accessed by {% page_header %}. Embeds page header.
@register.inclusion_tag("pages/header.html")
def page_header(page, current_slug):

    return {'page':page, 'current_slug':current_slug}
