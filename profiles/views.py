from django.shortcuts import get_object_or_404, render
from pages.models import Page
from social.models import Social
from profiles.models import Profile, Team
from django.core.urlresolvers import resolve

# Get all profiles for team page
def get_all_profiles(request):

    # Get team page
    page = get_object_or_404(Page, slug='team')

    # Get all profiles
    profiles = Profile.objects.all().order_by('order')

    # Get teams for dynamic navigation bar
    teams = Team.objects.only('title', 'slug')

    # Get current url for active links
    current_url = resolve(request.path_info).url_name

    context = {
        'page': page,
        'profiles': profiles,
        'teams': teams,
        'current_url': request.path
    }

    return render(request, 'profiles/index.html', context)

# Get specific profile
def get_profile(request, slug):

    # Get team page
    page = get_object_or_404(Page, slug='team')

    # Get profile by slug
    profile = get_object_or_404(Profile, slug=slug)

    # Get teams for dynamic navigation bar
    teams = Team.objects.only('title', 'slug')

    context = {
        'page': page,
        'profile': profile,
        'teams': teams
    }

    return render(request, 'profiles/profile.html', context)

# Get profiles by team
def get_profiles_by_team(request, slug):

    # Get team page
    page = get_object_or_404(Page, slug='team')

    # Get team by slug
    team = get_object_or_404(Team, slug=slug)

    # Get profiles that belong to the team
    profiles = team.profile_set.all()

    # Get teams for dynamic navigation bar
    teams = Team.objects.only('title', 'slug')

    # Get current url for active links
    current_url = resolve(request.path_info).url_name

    context = {
        'page': page,
        'profiles': profiles,
        'teams': teams,
        'current_url': current_url
    }

    return render(request, 'profiles/index.html', context)
