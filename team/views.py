from django.shortcuts import render
from team.models import TeamMember, Team

def index(request):
    page = get_object_or_404(TeamMember)

def team_member(request, slug):
    return HttpResponse("<h1>" + slug + "</h1>")
