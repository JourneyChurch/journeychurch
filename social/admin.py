from django.contrib import admin
from entries.admin import EntryAdmin
from social.models import Social

class SocialAdmin(EntryAdmin):
    """
    Manages admin for social entries
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Social Fields', {
            'fields': ('facebook', 'twitter', 'instagram', 'youtube', 'snapchat',)
        },)
    )

    # Show all objects in admin
    def get_queryset(self, request):
         return Social.all_objects.get_queryset()
         

admin.site.register(Social, SocialAdmin)
