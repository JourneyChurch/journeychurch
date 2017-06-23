from django.db import models

class Entry(models.Model):
    """
    Abstract class used to define fields for all entries
    """

    # ID - automatically generated

    # Title of entry
    title = models.CharField(max_length=100, unique=True, null=True)

    # Slug for entry
    slug = models.SlugField(max_length=200, unique=True, null=True)

    # Date created
    created_date = models.DateTimeField(auto_now_add=True, null=True)

    # Date updated
    updated_date = models.DateTimeField(auto_now=True, null=True)

    # Entry Date (used for scheduling)
    entry_date = models.DateTimeField(blank=True, null=True)

    # Entry Date (used for scheduling)
    expiration_date = models.DateTimeField(blank=True, null=True)

    # Representation in admin
    def __str__(self):
        return self.title


    class Meta:

        # Specifies that class is abstract and to add these fields to each model that extends it
        abstract = True
