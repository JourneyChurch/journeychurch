from django import template
from django.shortcuts import get_object_or_404
from pages.models import Content
from profiles.models import Team

register = template.Library()

# Team Section:
# Custom Tag that can be accessed by {% team %}. Creates fields for a three column type section
@register.inclusion_tag("pages/sections/team.html")
def team(section):

    # Assume empty initially
    profiles = None

    # Check if section team exists and is public
    try:
        team = Team.objects.get(id=section.team.id)
    except Team.DoesNotExist:
        team = None

    # If team exists and is public
    if team != None:
        profiles = team.profile_set.all()

    context = {
        'profiles': profiles,
    }

    return context
