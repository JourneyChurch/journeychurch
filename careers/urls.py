from django.conf.urls import url
from . import views

urlpatterns = [

    # Maps one career
    url(r'(?P<slug>[-\w]+)/$', views.get_career),

    # Maps all careers
    url(r'^$', views.get_all_careers),
]
