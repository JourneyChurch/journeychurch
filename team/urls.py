from django.conf.urls import url
from . import views

urlpatterns = [

    # Maps home page
    url(r'^$', views.index)
]
