from django.shortcuts import get_object_or_404, render
from pages.models import Page
from social.models import Social
from profiles.models import Profile, Team

# Get all profiles for team page
def get_all_profiles(request):
    page = get_object_or_404(Page.public_objects, slug='team')
    profiles = Profile.public_objects.all().order_by('order')

    # Get public navigation menu
    # Just hide navigation if not public
    try:
        if page.menu is None:
            navigation_menu = None
        else:
            navigation_menu = NavigationMenu.public_objects.get(pk=page.menu.id)
    except ObjectDoesNotExist:
        navigation_menu = None

    # Get public social
    # Just hide social if not public
    try:
        if profile.social is None:
            social = None
        else:
            social = Social.public_objects.get(pk=profile.social.id)
    except ObjectDoesNotExist:
        social = None

    # Get public content
    # Just hide content if not public
    ids = profile.teams_set.only("id")
    teams = Team.public_objects.filter(id__in=ids)

    context = {
        'title': page.display_title,
        'subtitle': page.subtitle,
        'link_url': page.link_url,
        'link_text': page.link_text,
        'background_image': page.background_image.url,
        'navigation_menu': navigation_menu,
        'profiles': profiles
    }

    return render(request, 'profiles/index.html', context)

# Get specific profile
def get_profile(request, slug):
    page = get_object_or_404(Page.public_objects, slug='team')
    profile = get_object_or_404(Profile.public_objects, slug=slug)

    # Get public navigation menu
    # Just hide navigation if not public
    try:
        if page.menu is None:
            navigation_menu = None
        else:
            navigation_menu = NavigationMenu.public_objects.get(pk=page.menu.id)
    except ObjectDoesNotExist:
        navigation_menu = None

    # Get public social
    # Just hide social if not public
    try:
        if profile.social is None:
            social = None
        else:
            social = Social.public_objects.get(pk=profile.social.id)
    except ObjectDoesNotExist:
        social = None

    # Get public content
    # Just hide content if not public
    ids = profile.teams_set.only("id")
    teams = Team.public_objects.filter(id__in=ids)

    context = {
        'title': page.display_title,
        'subtitle': page.subtitle,
        'link_url': page.link_url,
        'link_text': page.link_text,
        'background_image': page.background_image.url,
        'navigation_menu': navigation_menu,
        'profiles': profile
    }

    return render(request, 'profiles/profile.html', context)
