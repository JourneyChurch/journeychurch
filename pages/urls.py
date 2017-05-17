from django.conf.urls import url
from . import views

urlpatterns = [

    # Maps all slugs
    url(r'^(?P<slug>[-\w]+)/$', views.index),

    # Maps home page
    url(r'^$', views.index)
]
