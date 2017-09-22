from django.db import models
from entries.models import Entry

# Tinymce: wysiwyg editor for django admin
# https://github.com/aljosa/django-tinymce
from tinymce.models import HTMLField

class Career(Entry):
    """
    A career opening
    """

    # Summary of career
    summary = HTMLField(max_length=60000, blank=True, null=True)

    # Description of career
    description = HTMLField(max_length=60000, blank=True, null=True)

    # Name of contact
    contact_name = models.CharField(max_length=100, unique=True, null=True)

    # Email of contact
    contact_email = models.EmailField(max_length=254, null=True)
