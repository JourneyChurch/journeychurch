from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from pages.models import Page, Content


# Gets page by slug
def index(request, slug=None):

    # Homepage has a slug of home. If there is no slug(/) then get the home page
    if slug is None:
        page = get_object_or_404(Page, slug='home')
    else:
        page = get_object_or_404(Page, slug=slug)

    context = {
        'title': page.display_title,
        'subtitle': page.subtitle,
        'link_url': page.link_url,
        'link_text': page.link_text,
        'background_image': page.background_image.url,
        'navigation_menu': page.menu,
        'content': page.content_set.all()
    }

    return render(request, 'pages/index.html', context)
