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

    # Journeychurch.tv Facebook Page ID
    page_id = facebook["JOURNEYCHURCHTV"]["PAGE_ID"]

    # Page events api url
    page_events_api_fields = "attending_count,cover,description,end_time,name,owner,place,start_time,ticket_uri"
    page_events_api_url = "https://graph.facebook.com/{}/{}/events?fields={}".format(api_version, page_id, page_events_api_fields)


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


    # Get all facebook events
    def get_all_events(self, access_token):

        # Get events
        query_url = self.page_events_api_url

        # GET request for events using OAuth access token
        data = requests.get(query_url, headers={'Authorization': "OAuth {}".format(access_token)})

        # If successful extract json events
        if data.status_code == 200:
            data = data.json()

            events = data["data"]
            error = None
        else:
            events = None
            error = "Events could not be retrieved."

        return {
            "events": events,
            "error": error
        }
