from django.shortcuts import render
from django.http import Http404
from datetime import datetime, timedelta
from utils.acs.acs_connection import ACSConnection
from utils.facebook.facebook_connection import FacebookConnection
from utils.dates.format import format_date_month_day
from social.models import Social
from pages.models import SectionEvents
import json

# Get all events from ACS
def get_all_acs_events(request):

    # Default for start date is now
    start_date_default = datetime.now().strftime("%m/%d/%Y")

    # Default for stop date is 30 days in future
    stop_date_default = datetime.now() + timedelta(days=30)
    stop_date_default = stop_date_default.strftime("%m/%d/%Y")


    # Get start date query variable. If there isn't one, set to start date default
    start_date = request.GET.get("startdate", start_date_default)

    # Get stop date query variable. If there isn't one, set to stop date default
    stop_date = request.GET.get("stopdate", stop_date_default)

    # Get page index query variable. If there isn't one, set to 0
    page_index = request.GET.get("pageIndex", 0)

    # Get page size query variable. If there isn't one, set to 20
    page_size = request.GET.get("pageSize", 20)

    # Make acs connection
    acs_connection = ACSConnection()

    # Get events with start date
    data = acs_connection.get_all_events(start_date=start_date, stop_date=stop_date, page_index=page_index, page_size=page_size)

    context = {
        "events": data["events"],
        "error": data["error"],
        "page_count": data["page_count"],
        "page_index": data["page_index"],
        "page_size": data["page_size"],
        "start_date": start_date,
        "stop_date": stop_date
    }

    return render(request, 'events/acs/index.html', context)


# Get single event from ACS
def get_acs_event(request, id):

    # Make acs connection
    acs_connection = ACSConnection()

    # Get events with start date
    data = acs_connection.get_event(id=id)

    context = {
        "event": data["event"],
        "error": data["error"]
    }

    return render(request, 'events/acs/details.html', context)


# Get single event from Facebook
def get_facebook_event(request, event_id, page_id=174276778638):

    # Check if page id is a Journey Church affiliated page
    if not SectionEvents.objects.filter(facebook_page_id=page_id).exists():
        raise Http404

    # Create facebook connection
    facebook_connection = FacebookConnection(page_id=page_id)

    # Get access token
    data_access_token = facebook_connection.get_app_access_token()

    # If access token was retrieved
    if data_access_token["access_token"] != None:

        # Get all events using access token
        access_token = data_access_token["access_token"]
        data_event = facebook_connection.get_event(access_token, event_id)

        # If events were recieved
        if data_event["event"] != None:
            event = data_event["event"]
            error = None

        # If events were not recieved
        else:
            error = data_event["error"]
            event = None

    # If access token was not recieved
    else:
        error = data_access_token["error"]
        event = None

    # Get Journey Church social
    try:
        social = Social.objects.get(slug="journeychurchtv")
    except Social.DoesNotExist:
        social = None

    # Check for start time and end time
    if events["start_time"]:
        start_time = events["start_time"]
    else:
        start_time = None

    if events["end_time"]:
        end_time = events["end_time"]
    else:
        end_time = None

    context = {
        "event": event,
        "error": error,
        "access_token": access_token,
        "api_version": FacebookConnection.api_version,
        "date": format_date_month_day(start_time, end_time),
        "social": social
    }

    return render(request, 'events/facebook/details.html', context)


# Get all events from Facebook
def get_all_facebook_events(request, page_id=174276778638):

    # Check if page id is a Journey Church affiliated page
    if not SectionEvents.objects.filter(facebook_page_id=page_id).exists():
        raise Http404

    # Create facebook connection
    facebook_connection = FacebookConnection(page_id=page_id)

    # Get access token
    data_access_token = facebook_connection.get_app_access_token()

    # If access token was retrieved
    if data_access_token["access_token"] != None:

        # Get all events using access token
        access_token = data_access_token["access_token"]
        data_events = facebook_connection.get_events(access_token)

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

    context = {
        "events": events,
        "page_id": page_id,
        "error": error,
        "access_token": access_token,
        "api_version": FacebookConnection.api_version
    }

    return render(request, 'events/facebook/index.html', context)
