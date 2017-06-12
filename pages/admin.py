from django.contrib import admin
from pages.models import Page, NavigationMenu, NavigationItem, SectionDefault, SectionTwoColumn, SectionThreeColumn, SectionVideoGroup, SectionVideo


class PagesAdmin(admin.ModelAdmin):
    """
    Manages admin for pages
    """
    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}


class NavigationMenusAdmin(admin.ModelAdmin):
    """
    Manages admin for navigation menus
    """
    pass


class NavigationItemsAdmin(admin.ModelAdmin):
    """
    Manages admin for navigation items
    """
    # List title and menu that item belongs to
    list_display = ('title', 'menu')


class SectionDefaultAdmin(admin.ModelAdmin):
    """
    Manages admin for default sections
    """
    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}

    # List title and page that section belongs to
    list_display = ('title', 'page')


class SectionTwoColumnAdmin(admin.ModelAdmin):
    """
    Manages admin for two column sections
    """
    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}

    # List title and page that section belongs to
    list_display = ('title', 'page')


class SectionThreeColumnAdmin(admin.ModelAdmin):
    """
    Manages admin for three column sections
    """
    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}

    # List title and page that section belongs to
    list_display = ('title', 'page')


class SectionVideoGroupAdmin(admin.ModelAdmin):
    """
    Manages admin for video group section
    """
    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}

    # List title and page that section belongs to
    list_display = ('title', 'page')


class SectionVideoAdmin(admin.ModelAdmin):
    """
    Manages admin for video section
    """

    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}

    # List title and page that section belongs to
    list_display = ('title', 'page')


admin.site.register(Page, PagesAdmin)
admin.site.register(NavigationMenu, NavigationMenusAdmin)
admin.site.register(NavigationItem, NavigationItemsAdmin)
admin.site.register(SectionDefault, SectionDefaultAdmin)
admin.site.register(SectionTwoColumn, SectionTwoColumnAdmin)
admin.site.register(SectionThreeColumn, SectionThreeColumnAdmin)
admin.site.register(SectionVideoGroup, SectionVideoGroupAdmin)
admin.site.register(SectionVideo, SectionVideoAdmin)
