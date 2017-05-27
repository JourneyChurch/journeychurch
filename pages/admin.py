from django.contrib import admin
from pages.models import Page, NavigationMenu, NavigationItem, Content, SectionDefault, SectionTwoColumn, SectionThreeColumn


class PagesAdmin(admin.ModelAdmin):
    """
    Manages admin for pages
    """
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


class ContentAdmin(admin.ModelAdmin):
    """
    Manages content which contains sections
    """
    pass


class SectionDefaultAdmin(admin.ModelAdmin):
    """
    Manages admin for default sections
    """
    pass


class SectionTwoColumnAdmin(admin.ModelAdmin):
    """
    Manages admin for two column sections
    """
    pass


class SectionThreeColumnAdmin(admin.ModelAdmin):
    """
    Manages admin for three column sections
    """
    pass


admin.site.register(Page, PagesAdmin)
admin.site.register(NavigationMenu, NavigationMenusAdmin)
admin.site.register(NavigationItem, NavigationItemsAdmin)
admin.site.register(Content, ContentAdmin)
admin.site.register(SectionDefault, SectionDefaultAdmin)
admin.site.register(SectionTwoColumn, SectionTwoColumnAdmin)
admin.site.register(SectionThreeColumn, SectionThreeColumnAdmin)
