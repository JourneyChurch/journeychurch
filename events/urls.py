from django.conf.urls import url
from . import views

urlpatterns = [

    # Maps one series
    url(r'(?P<id>[-\w]+)/$', views.get_event),

    # Maps all series
    url(r'^$', views.get_all_events),

]
