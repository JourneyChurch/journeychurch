from django.shortcuts import get_object_or_404, render
from careers.models import Career
from pages.models import Page


# Show all careers
def get_all_careers(request):

    # Get careers page
    page = get_object_or_404(Page, slug='careers')

    # Get all careers
    careers = Career.objects.all()

    context = {
        "page": page,
        "careers": careers
    }

    return render(request, 'careers/index.html', context)


# Show one career
def get_career(request, slug):

    # Get careers page
    page = get_object_or_404(Page, slug='careers')

    # Get profile by slug
    career = get_object_or_404(Career, slug=slug)

    context = {
        "page": page,
        "career": career
    }

    return render(request, 'careers/details.html', context)
