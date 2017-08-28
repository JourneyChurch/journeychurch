from datetime import datetime
from journeychurch.config import acs
import requests

class ACSConnection:
    """
    ACS Connection class to use ACS Facility Scheduler REST API

    https://wiki.acstechnologies.com/display/DevCom/ACS+Facility+Scheduler+REST+API
    """

    # ACS Facility Scheduler Site ID
    site_id = acs["SITE_ID"]

    # Web Calendar ID
    calendar_id = acs["CALENDAR_ID"]

    # Api url
    api_url = "https://secure.accessacs.com/api_accessacs_mobile/v2/{}".format(site_id)

    # Username
    username = acs["USER"]

    # Password
    password = acs["PASSWORD"]

    # get events by date
    def get_all_events(self, start_date=None, stop_date=None, page_index=None, page_size=None):

        # Construct url for api request

        # Insert start and stop dates
        if start_date and stop_date:
            query_url = "{}/events?calendarids={}&startdate={}&stopdate={}".format(self.api_url, self.calendar_id, start_date, stop_date)
        elif start_date:
            query_url = "{}/events?calendarids={}&startdate={}".format(self.api_url, self.calendar_id, start_date, stop_date)
        elif stop_date:
            query_url = "{}/events?calendarids={}&stopdate={}".format(self.api_url, self.calendar_id, start_date, stop_date)
        else:
            query_url = "{}/events?calendarids={}".format(self.api_url, self.calendar_id, start_date, stop_date)

        # Insert page index other than default of 0
        if page_index:
            query_url = "{}&pageIndex={}".format(query_url, page_index)

        # Insert new page size other than default of 50 entries
        if page_size:
            query_url = "{}&pageSize={}".format(query_url, page_size)

        # Make GET request
        data = requests.get(query_url, auth=(self.username, self.password))
        error = None

        # List of events
        events = []

        # If successful, turn json into dictionary
        if data.status_code == 200:
            data = data.json()["Page"]

            # Add list of dictionaries for each event
            for event in data:
                events.append({
                    "name": event["EventName"],
                    "description": event["Description"],
                    "start_date": datetime.strptime(event["StartDate"], "%Y-%m-%d %H:%M:%S.%f"),
                    "id": event["EventId"]
                })

        # If unsuccessful give error message
        else:
            error = "There was a problem fetching events."

        # Return dictionary with events and errors
        return {
            "events": events,
            "error": error
        }


    # Get single event
    def get_event(self, id):

        # Construct url for api request
        query_url = "{}/events/{}".format(self.api_url, id)

        # Make api request
        data = requests.get(query_url, auth=(self.username, self.password))
        error = None

        # Event
        event = {}

        # If successful, turn json into dictionary
        if data.status_code == 200:
            data = data.json()

            event["name"] = data["EventName"]
            event["description"] = data["Description"]
            event["location"] = data["Location"]
            event["start_date"] = data["StartDate"]
            event["stop_date"] = data["StopDate"]
            event["registration_allowed"] = data["AllowRegistration"]

        # If unsuccessful give error message
        else:
            error = "This is event could not be found"

        return {
            "event": event,
            "error": error
        }
