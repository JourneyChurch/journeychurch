from django.contrib import admin
from entries.admin import EntryAdmin
from pages.models import Page, NavigationMenu, NavigationItem, SectionDefault, SectionTwoColumn, SectionThreeColumn, SectionVideoGroup, SectionVideo


class PagesAdmin(EntryAdmin):
    """
    Manages admin for pages
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Page Fields', {
            'fields': ('display_title', 'subtitle', 'link_url', 'link_text', 'background_image', 'menu', 'social')
        },)
    )


class NavigationItemsAdmin(EntryAdmin):
    """
    Manages admin for navigation items
    """

    # List title and menu that item belongs to
    list_display = ('title', 'menu')

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Navigation Item Fields', {
            'fields': ('url', 'new_tab', 'order', 'menu')
        },)
    )


class ContentAdmin(EntryAdmin):
    """
    Manages admin for all content
    """

    # List title and page that section belongs to
    list_display = ('title', 'page')


class SectionDefaultAdmin(ContentAdmin):
    """
    Manages admin for default section template
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Section Fields', {
            'fields': ('display_title', 'page', 'background_image', 'background_color', 'order', 'content', 'image')
        },)
    )

class SectionTwoColumnAdmin(ContentAdmin):
    """
    Manages admin for two column section template
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Section Fields', {
            'fields': ('display_title', 'page', 'background_image', 'background_color', 'order', 'center_text')
        },),
        ('Column Left', {
            'fields': ('title_left', 'content_left', 'image_left')
        },),
        ('Column Right', {
            'fields': ('title_right', 'content_right', 'image_right')
        },)
    )

class SectionThreeColumnAdmin(ContentAdmin):
    """
    Manages admin for three column section template
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Section Fields', {
            'fields': ('display_title', 'page', 'background_image', 'background_color', 'order', 'center_text')
        },),
        ('Column Left', {
            'fields': ('title_left', 'content_left', 'image_left')
        },),
        ('Column Center', {
            'fields': ('title_center', 'content_center', 'image_center')
        },),
        ('Column Right', {
            'fields': ('title_right', 'content_right', 'image_right')
        },)
    )


class SectionVideoGroupAdmin(ContentAdmin):
    """
    Manages admin for video group section template
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Section Fields', {
            'fields': ('video_group',)
        },)
    )

class SectionVideoAdmin(ContentAdmin):
    """
    Manages admin for video section template
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Section Fields', {
            'fields': ('video',)
        },)
    )



admin.site.register(Page, PagesAdmin)
admin.site.register(NavigationMenu, EntryAdmin)
admin.site.register(NavigationItem, NavigationItemsAdmin)
admin.site.register(SectionDefault, SectionDefaultAdmin)
admin.site.register(SectionTwoColumn, SectionTwoColumnAdmin)
admin.site.register(SectionThreeColumn, SectionThreeColumnAdmin)
admin.site.register(SectionVideoGroup, SectionVideoGroupAdmin)
admin.site.register(SectionVideo, SectionVideoAdmin)
