from django import template
from django.shortcuts import get_object_or_404
from pages.models import NavigationMenu, NavigationItem
from django.core.exceptions import ObjectDoesNotExist

register = template.Library()

# Navigation menu:
# Custom Tag that can be accessed by {% navigation %}. Sends NavigationMenu items to navigation.html.
@register.inclusion_tag("pages/navigation_menu.html")
def navigation_menu(current_slug, title='Main', inline=True, mobile=False):

    # get navigation menu
    try:
        menu = NavigationMenu.objects.get(title=title)
    except ObjectDoesNotExist:
        menu = None

    # get all of its navigation items
    if menu:
        try:
            navigation_items = NavigationItem.objects.filter(menu_id=menu.id).order_by('order')
        except ObjectDoesNotExist:
            navigation_items = None
    else:
        navigation_items = None

    return {'navigation_items': navigation_items, 'current_slug':current_slug, 'inline': inline, 'title': title, 'mobile': mobile}
