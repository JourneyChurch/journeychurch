from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from pages.models import Page, NavigationMenu, NavigationItem


# Gets page by slug
def index(request, slug=None):

    # Homepage has a slug of home. If there is no slug(/) then get the home page
    if slug is None:
        page = get_object_or_404(Page, slug='home')

    # Otherwise get the page that matches the slug
    else:
        page = get_object_or_404(Page, slug=slug)

    if page.menu == None:
        navigation_items = None
    else:
        navigation_items = page.menu.navigationitem_set.all()

    context = {
        'title': page.display_title,
        'subtitle': page.subtitle,
        'link_url': page.link_url,
        'link_text': page.link_text,
        'image': page.image.url,
        'navigation_items': navigation_items
    }

    return render(request, 'pages/index.html', context)
