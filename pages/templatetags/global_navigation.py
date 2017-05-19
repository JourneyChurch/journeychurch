from django import template
from django.shortcuts import get_object_or_404
from pages.models import NavigationMenu

register = template.Library()

# Custom Tag that can be accessed by {{ global_navigation }}. Sends NavigationMenu 'main' items to global_navigation.html.
@register.inclusion_tag("pages/global_navigation.html")
def global_navigation():

    # get navigation menu main
    menu = get_object_or_404(NavigationMenu, title='main')

    # get all of its navigation items
    navigation_items = menu.navigationitem_set.all()

    return {'navigation_items': navigation_items}
