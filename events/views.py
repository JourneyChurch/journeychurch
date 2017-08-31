from django.shortcuts import render
from datetime import datetime, timedelta
from utils.acs.acs_connection import ACSConnection
import json

# Get all events from ACS
def get_all_events(request):

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

    return render(request, 'events/index.html', context)


# Get single event from ACS
def get_event(request, id):

    # Make acs connection
    acs_connection = ACSConnection()

    # Get events with start date
    data = acs_connection.get_event(id=id)

    context = {
        "event": data["event"],
        "error": data["error"]
    }

    return render(request, 'events/details.html', context)
