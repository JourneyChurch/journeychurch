from django.db import models
from social.models import Social

# Tinymce: wysiwyg editor for django admin
# https://github.com/aljosa/django-tinymce
from tinymce.models import HTMLField


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
    order = models.CharField(max_length=100, unique=True)

    # Foreign key to relate a navigation item to a menu
    menu = models.ForeignKey(NavigationMenu, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


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
    background_image = models.ImageField(upload_to="backgrounds/", max_length=200)

    # Associated navigation menu with page
    menu = models.ForeignKey(NavigationMenu, on_delete=models.CASCADE, null=True, blank=True)

    # Social media links
    social = models.ForeignKey(Social, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    """
    Base Class for all content.
    This allows a page to have different types of sections.
    A One to one field is automatically created between Content and
    different kinds of sections using multi table inheritance
    """

    # Title of content
    title = models.CharField(max_length=100)

    # Display Title
    display_title = models.CharField(max_length=100, blank=True)

    # Page that content belongs to
    page = models.ForeignKey(Page, on_delete=models.CASCADE)

    # Background image (uploads to /media/uploads/backgrounds/)
    background_image = models.ImageField(upload_to="backgrounds/", max_length=200, blank=True)

    # Background color in hex
    background_color = models.CharField(max_length=6, default="f3f3f3")

    # Order of section
    order = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.title


class SectionDefault(Content):
    """
    Section with one column of content
    """

    # main content
    content = HTMLField(max_length=60000, blank=True)

    # main image
    image = models.ImageField(upload_to="content/", max_length=200, blank=True)


class SectionTwoColumn(Content):
    """
    Section with two columns of content
    """

    # Left title
    title_left = models.CharField(max_length=100, blank=True)

    # Left column content
    content_left = HTMLField(max_length=60000, blank=True)

    # Left image
    image_left = models.ImageField(upload_to="content/", max_length=200, blank=True)

    # Right title
    title_right = models.CharField(max_length=100, blank=True)

    # Right column content
    content_right = HTMLField(max_length=60000, blank=True)

    # Left image
    image_right = models.ImageField(upload_to="content/", max_length=200, blank=True)

    # Center all text
    center_text = models.BooleanField(default=False)


class SectionThreeColumn(Content):
    """
    Section with three columns of content
    """

    # Left title
    title_left = models.CharField(max_length=100, blank=True)

    # Left column content
    content_left = HTMLField(max_length=60000, blank=True)

    # Left image
    image_left = models.ImageField(upload_to="content/", max_length=200, blank=True)

    # Center title
    title_center = models.CharField(max_length=100, blank=True)

    # Center column content
    content_center = HTMLField(max_length=60000, blank=True)

    # Center image
    image_center = models.ImageField(upload_to="content/", max_length=200, blank=True)

    # Right title
    title_right = models.CharField(max_length=100, blank=True)

    # Right column content
    content_right = HTMLField(max_length=60000, blank=True)

    # Left image
    image_right = models.ImageField(upload_to="content/", max_length=200, blank=True)

    # Center all text
    center_text = models.BooleanField(default=False)
