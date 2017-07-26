from django.shortcuts import get_object_or_404, render
from pages.models import Page
from social.models import Social
from profiles.models import Profile, Team

# Get all profiles for team page
def get_all_profiles(request):
    page = get_object_or_404(Page.public_objects, slug='team')
    profiles = Profile.public_objects.all().order_by('order')
    teams = Team.public_objects.only('title', 'slug')

    context = {
        'page': page,
        'profiles': profiles,
        'teams': teams
    }

    return render(request, 'profiles/index.html', context)

# Get specific profile
def get_profile(request, slug):
    page = get_object_or_404(Page.public_objects, slug='team')
    profile = get_object_or_404(Profile.public_objects, slug=slug)
    teams = Team.public_objects.only('title', 'slug')

    context = {
        'page': page,
        'profile': profile,
        'teams': teams
    }

    return render(request, 'profiles/profile.html', context)
