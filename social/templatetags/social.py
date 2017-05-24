from django import template
from django.shortcuts import get_object_or_404
from social.models import Social

register = template.Library()

# Social Media:
# Custom Tag that can be accessed by {{ social }}. Sends Social to social.html for embedding social media links in page.
@register.inclusion_tag("social/social.html")
def social(title="Main"):

    # get social
    social = get_object_or_404(Social, title=title)

    return {'social': social}
