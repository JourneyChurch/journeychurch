from django.db import models
from entries.models import Entry
from social.models import Social
from media.models import VideoGroup, Video
from profiles.models import Team

# Tinymce: wysiwyg editor for django admin
# https://github.com/aljosa/django-tinymce
from tinymce.models import HTMLField


class NavigationMenu(Entry):
    """
    Menu that has navigation items.
    This menu is associated with a page or part of application.
    """

    class Meta:
        # Plural name used in admin
        verbose_name_plural = "Navigation - Menus"


class NavigationItem(Entry):
    """
    Navigation item that belongs to a menu.
    """

    # Displayed title of navigation item
    display_title = models.CharField(max_length=100, null=True)

    # Url to link to
    url = models.CharField(max_length=2000, null=True)

    # New tab
    new_tab = models.BooleanField(default=False)

    # Order of navigation item in menu
    order = models.CharField(max_length=100, null=True)

    # Foreign key to relate a navigation item to a menu
    menu = models.ForeignKey(NavigationMenu, on_delete=models.CASCADE)

    class Meta:
        # Plural name used in admin
        verbose_name_plural = "Navigation - Items"


class Page(Entry):
    """
    A single page without content
    where an image, title, and navigation can be found.

    The content is derived from different Sections that belong to the page.
    """

    # Title display on page
    display_title = models.CharField(max_length=100, null=True)

    # Sub title under display title
    subtitle = models.CharField(max_length=100, blank=True, null=True)

    # Button link to a URL
    link_url = models.CharField(max_length=2000, blank=True, null=True)

    # Button link text
    link_text = models.CharField(max_length=100, blank=True, null=True)

    # Background image (uploads to /uploads/backgrounds/)
    background_image = models.ImageField(upload_to="backgrounds/", max_length=200)

    # Associated navigation menu with page
    menu = models.ForeignKey(NavigationMenu, on_delete=models.CASCADE, null=True, blank=True)

    # Social media links
    social = models.ForeignKey(Social, on_delete=models.CASCADE, null=True, blank=True)


class Content(Entry):
    """
    Base Class for all content.
    This allows a page to have different types of sections.
    A One to one field is automatically created between Content and
    different kinds of sections using multi table inheritance
    """

    # Display Title
    display_title = models.CharField(max_length=100, blank=True, null=True)

    # Page that content belongs to
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True)

    # Background image (uploads to /uploads/backgrounds/)
    background_image = models.ImageField(upload_to="backgrounds/", max_length=200, blank=True, null=True)

    # Background color in hex
    background_color = models.CharField(max_length=6, blank=True, null=True)

    # Order of section
    order = models.CharField(max_length=100, null=True)

    # Determine the section type
    # The attributes are lowercase names of the class names below
    def section_type(self):
        if hasattr(self, "sectiondefault"):
            return "default"
        elif hasattr(self, "sectiontwocolumn"):
            return "twocolumn"
        elif hasattr(self, "sectionthreecolumn"):
            return "threecolumn"
        elif hasattr(self, "sectionvideogroup"):
            return "videogroup"
        elif hasattr(self, "sectionvideo"):
            return "video"
        elif hasattr(self, "sectionseries"):
            return "series"
        elif hasattr(self, "sectionteam"):
            return "team"
        return None


class SectionDefault(Content):
    """
    Section with one column of content
    """

    # Multi table inheritance pointer to Content
    content_ptr = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, default=None)

    # main content
    content = HTMLField(max_length=60000, null=True)

    # main image
    image = models.ImageField(upload_to="content/", max_length=200, blank=True, null=True)

    class Meta:
        """
        Plural name used in admin
        """

        verbose_name_plural = "Sections - Default Template"


class SectionTwoColumn(Content):
    """
    Section with two columns of content
    """

    # Multi table inheritance pointer to Content
    content_ptr = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, default=None)

    # Left title
    title_left = models.CharField(max_length=100, blank=True, null=True)

    # Left column content
    content_left = HTMLField(max_length=60000, blank=True, null=True)

    # Left image
    image_left = models.ImageField(upload_to="content/", max_length=200, blank=True, null=True)

    # Right title
    title_right = models.CharField(max_length=100, blank=True, null=True)

    # Right column content
    content_right = HTMLField(max_length=60000, blank=True, null=True)

    # Left image
    image_right = models.ImageField(upload_to="content/", max_length=200, blank=True, null=True)

    # Center all text
    center_text = models.BooleanField(default=False)

    class Meta:
        """
        Plural name used in admin
        """

        verbose_name_plural = "Sections - Two Column Template"


class SectionThreeColumn(Content):
    """
    Section with three columns of content
    """

    # Multi table inheritance pointer to Content
    content_ptr = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, default=None)

    # Left title
    title_left = models.CharField(max_length=100, blank=True, null=True)

    # Left column content
    content_left = HTMLField(max_length=60000, blank=True, null=True)

    # Left image
    image_left = models.ImageField(upload_to="content/", max_length=200, blank=True, null=True)

    # Center title
    title_center = models.CharField(max_length=100, blank=True, null=True)

    # Center column content
    content_center = HTMLField(max_length=60000, blank=True, null=True)

    # Center image
    image_center = models.ImageField(upload_to="content/", max_length=200, blank=True, null=True)

    # Right title
    title_right = models.CharField(max_length=100, blank=True, null=True)

    # Right column content
    content_right = HTMLField(max_length=60000, blank=True, null=True)

    # Left image
    image_right = models.ImageField(upload_to="content/", max_length=200, blank=True, null=True)

    # Center all text
    center_text = models.BooleanField(default=False)

    class Meta:
        """
        Plural name used in admin
        """

        verbose_name_plural = "Sections - Three Column Template"


class SectionVideoGroup(Content):
    """
    Section for video group
    """

    # Multi table inheritance pointer to Content
    content_ptr = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, default=None)

    # Video Group
    video_group = models.ForeignKey(VideoGroup, on_delete=models.CASCADE)

    class Meta:
        """
        Plural name used in admin
        """

        verbose_name_plural = "Sections - Video Group Template"


class SectionVideo(Content):
    """
    Section for video
    """

    # Multi table inheritance pointer to Content
    content_ptr = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, default=None)

    # Video Group
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        """
        Plural name used in admin
        """

        verbose_name_plural = "Sections - Single Video Template"


class SectionSeries(Content):
    """
    Section for series
    """

    # Multi table inheritance pointer to Content
    content_ptr = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, default=None)

    # Type of series
    SERIES_TYPES = (
        ('weekend', 'Weekend'),
        ('college', 'College'),
    )
    series_type = models.CharField(max_length=7, choices=SERIES_TYPES, default='weekend')

    class Meta:
        """
        Plural name used in admin
        """

        verbose_name_plural = "Sections - Series Template"


class SectionTeam(Content):
    """
    Section for team
    """

    # Multi table inheritance pointer to Content
    content_ptr = models.OneToOneField(Content, on_delete=models.CASCADE, parent_link=True, default=None)

    # Video Group
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    class Meta:
        """
        Plural name used in admin
        """

        verbose_name_plural = "Sections - Team Template"
