from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from pages.models import Page, Content, NavigationMenu
from django.core.exceptions import ObjectDoesNotExist


# Gets page by slug
def index(request, slug=None):

    # Homepage has a slug of home. If there is no slug(/) then get the home page
    if slug is None:
        page = get_object_or_404(Page.public_objects, slug='home')
    else:
        page = get_object_or_404(Page.public_objects, slug=slug)

    # Get public navigation menu
    try:
        navigation_menu = NavigationMenu.public_objects.get(pk=page.menu.id)
    except ObjectDoesNotExist:
        navigation_menu = None

    context = {
        'title': page.display_title,
        'subtitle': page.subtitle,
        'link_url': page.link_url,
        'link_text': page.link_text,
        'background_image': page.background_image.url,
        'navigation_menu': navigation_menu,
        'content': page.content_set.all()
    }

    return render(request, 'pages/index.html', context)
