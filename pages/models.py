from django.db import models
from social.models import Social


class NavigationMenu(models.Model):
    """
    Menu that has navigation items.
    This menu is associated with a page or part of application.
    """

    # Title of navigation menu, must be unique (not displayed, just for organization)
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class NavigationItem(models.Model):
    """
    Navigation item that belongs to a menu.
    """

    # Title of navigation item
    title = models.CharField(max_length=100)

    # Url to link to
    url = models.CharField(max_length=2000)

    # New tab
    new_tab = models.BooleanField(default=False)

    # Order of navigation item in menu
    order = models.CharField(max_length=100)

    # Foreign key to relate a navigation item to a menu
    menu = models.ForeignKey(NavigationMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Section(models.Model):
    """
    """


class SectionDefault(models.Model):
    """
    """


class SectionTwoColumns(models.Model):
    """
    """


class SectionThreeColumn(models.Model):
    """
    """


class SectionVideo(models.Model):
    """
    """


class Page(models.Model):
    """
    A single page without content
    where an image, title, and navigation can be found.

    The content is derived from different Sections that belong to the page.
    """

    # Title of page, must be unique (not displayed, just for organization)
    title = models.CharField(max_length=100, unique=True)

    # Title display on page
    display_title = models.CharField(max_length=100)

    # Slug based off of display title
    slug = models.SlugField(max_length=200, unique=True, blank=True)

    # Sub title under display title
    subtitle = models.CharField(max_length=100, blank=True)

    # Button link to a URL
    link_url = models.CharField(max_length=2000, blank=True)

    # Button link text
    link_text = models.CharField(max_length=100, blank=True)

    # Background image (uploads to /media/uploads/backgrounds/)
    image = models.ImageField(upload_to="backgrounds/", max_length=200)

    # Associated navigation menu with page
    menu = models.ForeignKey(NavigationMenu, on_delete=models.CASCADE, null=True, blank=True)

    # Social media links
    social = models.ForeignKey(Social, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
