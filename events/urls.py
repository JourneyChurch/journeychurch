from django.conf.urls import url
from . import views

urlpatterns = [

    # Maps one acs event
    url(r'all/(?P<id>[-\w]+)/$', views.get_acs_event),

    # Maps all acs events
    url(r'all/$', views.get_all_acs_events),

    # Maps one acs event
    url(r'(?P<id>[-\w]+)/$', views.get_facebook_event),

    # Maps all acs events
    url(r'^$', views.get_all_facebook_events),

]
