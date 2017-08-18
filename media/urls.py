from django.conf.urls import url
from . import views

urlpatterns = [

    # Maps one series
    url(r'series/(?P<slug>[-\w]+)/$', views.get_series),

    # Maps all series
    url(r'series/$', views.get_all_series),

    #   Maps one experience
    url(r'experiences/(?P<slug>[-\w]+)/$', views.get_experience, name='get_experience'),

    # Maps all experiences
    url(r'experiences/$', views.get_all_experiences),

    # Maps one video group
    url(r'watch/group/(?P<slug>[-\w]+)/$', views.get_video_group),

    # Maps one video
    url(r'watch/(?P<slug>[-\w]+)/$', views.get_video),
]
