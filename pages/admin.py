from django.contrib import admin
from entries.admin import EntryAdmin
from pages.models import Page, NavigationMenu, NavigationItem, SectionDefault, SectionTwoColumn, SectionThreeColumn, SectionVideoGroup, SectionVideo, SectionTeam


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

    # Show all objects in admin
    def get_queryset(self, request):
         return Page.all_objects.get_queryset()


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
            'fields': ('display_title', 'url', 'new_tab', 'order', 'menu')
        },)
    )

    # Show all objects in admin
    def get_queryset(self, request):
         return NavigationItem.all_objects.get_queryset()


class NavigationMenuAdmin(EntryAdmin):
    """
    Manages admin for navigation items
    """

    # Show all objects in admin
    def get_queryset(self, request):
         return NavigationMenu.all_objects.get_queryset()


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

    # Show all objects in admin
    def get_queryset(self, request):
         return SectionDefault.all_objects.get_queryset()

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

    # Show all objects in admin
    def get_queryset(self, request):
         return SectionTwoColumn.all_objects.get_queryset()

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

    # Show all objects in admin
    def get_queryset(self, request):
         return SectionThreeColumn.all_objects.get_queryset()


class SectionVideoGroupAdmin(ContentAdmin):
    """
    Manages admin for video group section template
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Section Fields', {
            'fields': ('display_title', 'page', 'background_image', 'background_color', 'order')
        },),
        ('Video Group Fields', {
            'fields': ('video_group',)
        },)
    )

    # Show all objects in admin
    def get_queryset(self, request):
         return SectionVideoGroup.all_objects.get_queryset()


class SectionVideoAdmin(ContentAdmin):
    """
    Manages admin for video section template
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Section Fields', {
            'fields': ('display_title', 'page', 'background_image', 'background_color', 'order')
        },),
        ('Video Fields', {
            'fields': ('video',)
        },)
    )

    # Show all objects in admin
    def get_queryset(self, request):
         return SectionVideo.all_objects.get_queryset()


class SectionTeamAdmin(ContentAdmin):
    """
    Manages team admin
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Section Fields', {
            'fields': ('display_title', 'page', 'background_image', 'background_color', 'order')
        },),
        ('Team Fields', {
            'fields': ('team',)
        },)
    )

    # Show all objects in admin
    def get_queryset(self, request):
         return SectionTeam.all_objects.get_queryset()



admin.site.register(Page, PagesAdmin)
admin.site.register(NavigationMenu, NavigationMenuAdmin)
admin.site.register(NavigationItem, NavigationItemsAdmin)
admin.site.register(SectionDefault, SectionDefaultAdmin)
admin.site.register(SectionTwoColumn, SectionTwoColumnAdmin)
admin.site.register(SectionThreeColumn, SectionThreeColumnAdmin)
admin.site.register(SectionVideoGroup, SectionVideoGroupAdmin)
admin.site.register(SectionVideo, SectionVideoAdmin)
admin.site.register(SectionTeam, SectionTeamAdmin)
