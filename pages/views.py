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

    context = {
        'title': page.display_title,
        'subtitle': page.subtitle,
        'link': page.link,
        'link_text': page.link_text,
        'image': page.image.url,
        'navigation_links': page.navigation.navigationitem_set.all()
    }

    return render(request, 'pages/index.html', context)
