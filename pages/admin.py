from django.contrib import admin
from pages.models import Page, NavigationMenu, NavigationItem


class PagesAdmin(admin.ModelAdmin):
    """
    Manages admin for pages
    """
    prepopulated_fields = {'slug': ('display_title',)}


class NavigationMenusAdmin(admin.ModelAdmin):
    """
    Manages admin for navigation menus
    """
    pass


class NavigationItemsAdmin(admin.ModelAdmin):
    """
    Manages admin for navigation items
    """
    pass


admin.site.register(Page, PagesAdmin)
admin.site.register(NavigationMenu, NavigationMenusAdmin)
admin.site.register(NavigationItem, NavigationItemsAdmin)
