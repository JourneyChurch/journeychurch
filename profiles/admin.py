from django.contrib import admin
from entries.admin import EntryAdmin
from profiles.models import Profile, Team

class ProfilesAdmin(EntryAdmin):
    """
    Manages admin for profiles
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Profile Fields', {
            'fields': ('job_title', 'bio', 'email', 'image', 'social', 'teams', 'order')
        },)
    )

class TeamAdmin(EntryAdmin):
    """
    Manages admin for teams
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
    )

admin.site.register(Profile, ProfilesAdmin)
admin.site.register(Team, TeamAdmin)
