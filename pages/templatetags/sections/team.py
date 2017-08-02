from django import template
from django.shortcuts import get_object_or_404
from pages.models import Content

register = template.Library()

# Three Column Section:
# Custom Tag that can be accessed by {% team %}. Creates fields for a three column type section
@register.inclusion_tag("pages/sections/team.html")
def team(section):

    # Get profiles from section team
    profiles = section.team.profile_set.all()

    context = {
        'profiles': profiles,
    }

    return context
