from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from pages.models import Page, Content, NavigationMenu
from django.core.exceptions import ObjectDoesNotExist


# Gets page by slug
def index(request, slug=None):

    # Homepage has a slug of home. If there is no slug(/) then get the home page
    # Throw 404 if page not public
    if slug is None:
        page = get_object_or_404(Page.public_objects, slug='home')
    else:
        page = get_object_or_404(Page.public_objects, slug=slug)

    # Get public navigation menu
    # Just hide navigation if not public
    try:
        if page.menu is None:
            navigation_menu = None
        else:
            navigation_menu = NavigationMenu.public_objects.get(pk=page.menu.id)
    except ObjectDoesNotExist:
        navigation_menu = None

    # Get public content
    # Just hide content if not public
    ids = page.content_set.only("id")
    content = Content.public_objects.filter(id__in=ids)

    # Context for view
    context = {
        'page': {
            'title': page.display_title,
            'subtitle': page.subtitle,
            'link_url': page.link_url,
            'link_text': page.link_text,
            'background_image': page.background_image.url,
            'navigation_menu': navigation_menu,
        },
        'content': content
    }

    return render(request, 'pages/index.html', context)
