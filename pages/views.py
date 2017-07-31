from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from pages.models import Page, NavigationMenu
from django.core.exceptions import ObjectDoesNotExist


# Gets page by slug
def index(request, slug=None):

    # Homepage has a slug of home. If there is no slug(/) then get the home page
    # Throw 404 if page not public
    if slug is None:
        page = get_object_or_404(Page, slug='home')
    else:
        page = get_object_or_404(Page, slug=slug)


    # Context for view
    context = {
        'page': page,
        'content': page.content_set.all(),
    }

    return render(request, 'pages/index.html', context)
