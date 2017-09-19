from django import template
from django.shortcuts import get_object_or_404
from utils.facebook.facebook_connection import FacebookConnection
from social.models import Social

register = template.Library()

# Events Section:
# Custom Tag that can be accessed by {% events %}. Creates fields for an events type section
@register.inclusion_tag("pages/sections/events.html")
def events(section):

    # Create a Facebook Connection to Facebook page
    facebook_connection = FacebookConnection(page_id=section.facebook_page_id)

    # Get access token
    data_access_token = facebook_connection.get_app_access_token()

    # If access token was retrieved
    if data_access_token["access_token"] != None:

        # Get all events using access token
        access_token = data_access_token["access_token"]
        data_events = facebook_connection.get_events(access_token=access_token, limit=3)

        # If events were recieved
        if data_events["events"] != None:
            events = data_events["events"]
            error = None

        # If events were not recieved
        else:
            error = data_events["error"]
            events = None

    # If access token was not recieved
    else:
        error = data_access_token["error"]
        events = None

    try:
        social = Social.objects.get(id=section.social.id)
    except Social.DoesNotExist:
        social = None

    context = {
        "access_token": access_token,
        "events": events,
        "social": social,
        "page_id": section.facebook_page_id
    }

    return context
