from datetime import datetime
from journeychurch.config import facebook
import requests

class FacebookConnection:
    """
    Facebook Connection class for Facebook Graph API

    Page Events API: https://developers.facebook.com/docs/graph-api/reference/page/events/
    """

    # Api version
    api_version = "v2.7"

    # Facebook App ID
    app_id = facebook["APP_ID"]

    # Facebook App secret
    app_secret = facebook["APP_SECRET"]


    # Constructor takes app id for different facebook pages
    def __init__(self, page_id):
        self.page_id = page_id


    # Get app access token
    def get_app_access_token(self):

        # App access token query
        query_url = "https://graph.facebook.com/oauth/access_token?client_id={}&client_secret={}&grant_type=client_credentials".format(self.app_id, self.app_secret)

        # GET request for access token
        data = requests.get(query_url)

        # If successful extract access token
        if data.status_code == 200:
            data = data.json()

            access_token = data["access_token"]
            error = None
        else:
            access_token = None
            error = "Could not connect to events server."

        return {
            "access_token": access_token,
            "error": error
        }


    # Get single facebook event
    def get_event(self, access_token, event_id):

        # Page events api url
        event_api_url = "https://graph.facebook.com/{}/{}?fields=".format(self.api_version, event_id)

        # Api fields to get
        api_fields = "attending_count,description,end_time,name,place,start_time,ticket_uri"

        # Get events
        query_url = event_api_url + api_fields

        # GET request for events using OAuth access token
        data = requests.get(query_url, headers={'Authorization': "OAuth {}".format(access_token)})

        # If successful extract json events
        if data.status_code == 200:
            event = data.json()

            # Convert start and end times to datetime objects
            event["end_time"] = datetime.strptime(event["end_time"], "%Y-%m-%dT%H:%M:%S-%f")
            event["start_time"] = datetime.strptime(event["start_time"], "%Y-%m-%dT%H:%M:%S-%f")

            error = None
        else:
            event = None
            error = "This event could not be found."

        return {
            "event": event,
            "error": error
        }

    # Get all facebook events
    def get_all_events(self, access_token):

        # Page events api url
        page_events_api_url = "https://graph.facebook.com/{}/{}/events?fields=".format(self.api_version, self.page_id)

        # Api fields to get
        api_fields = "cover,end_time,name,place,start_time"

        # Get events
        query_url = page_events_api_url + api_fields

        # GET request for events using OAuth access token
        data = requests.get(query_url, headers={'Authorization': "OAuth {}".format(access_token)})

        # If successful extract json events
        if data.status_code == 200:
            data = data.json()

            events = data["data"]
            error = None
        else:
            events = None
            error = "No events could be found."

        return {
            "events": events,
            "error": error
        }
