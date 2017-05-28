from django.contrib import admin
from pages.models import Page, NavigationMenu, NavigationItem, SectionDefault, SectionTwoColumn, SectionThreeColumn


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
    list_display = ('title', 'menu')


class SectionDefaultAdmin(admin.ModelAdmin):
    """
    Manages admin for default sections
    """
    pass
    prepopulated_fields = {'slug': ('title',)}


class SectionTwoColumnAdmin(admin.ModelAdmin):
    """
    Manages admin for two column sections
    """
    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}


class SectionThreeColumnAdmin(admin.ModelAdmin):
    """
    Manages admin for three column sections
    """
    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Page, PagesAdmin)
admin.site.register(NavigationMenu, NavigationMenusAdmin)
admin.site.register(NavigationItem, NavigationItemsAdmin)
admin.site.register(SectionDefault, SectionDefaultAdmin)
admin.site.register(SectionTwoColumn, SectionTwoColumnAdmin)
admin.site.register(SectionThreeColumn, SectionThreeColumnAdmin)
