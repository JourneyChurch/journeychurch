from django.db import models
from social.models import Social
from entries.models import Entry

# Tinymce: wysiwyg editor for django admin
# https://github.com/aljosa/django-tinymce
from tinymce.models import HTMLField


class Team(Entry):
    """
    A Team that has people as profiles
    """

    pass


class Profile(Entry):
    """
    A profile representing a person
    """

    # Job title of person
    job_title = models.CharField(max_length=100, unique=True, null=True)

    # Biography
    bio = HTMLField(max_length=60000, null=True)

    # Email
    email = models.EmailField(max_length=254, null=True)

    # image (uploads to /uploads/team/)
    image = models.ImageField(upload_to="team/", max_length=200)

    # Social media links
    social = models.ForeignKey(Social, on_delete=models.CASCADE, null=True, blank=True)

    # Order of person in team
    order = models.CharField(max_length=100, null=True)

    # Teams that the team member belongs to
    teams = models.ManyToManyField(Team, blank=True)
