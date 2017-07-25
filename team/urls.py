from django.conf.urls import url
from . import views

urlpatterns = [

    # Maps specific team member
    url(r'^(?P<slug>[-\w]+)/$', views.team_member),

    # Maps home page
    url(r'^$', views.index),
]
