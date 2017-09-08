from django.conf.urls import url
from . import views

urlpatterns = [

    # Maps one acs event
    url(r'all/(?P<id>[-\w]+)/$', views.get_acs_event),

    # Maps all acs events
    url(r'all/$', views.get_all_acs_events),

    # Maps one facebook event by page id
    url(r'(?P<page_id>[-\w]+)/(?P<event_id>[-\w]+)/$', views.get_facebook_event),

    # Maps all facebook events by page id
    url(r'(?P<page_id>[-\w]+)/$', views.get_all_facebook_events),

    # Maps all main facebook events
    url(r'^$', views.get_all_facebook_events),

]
