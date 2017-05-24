from django.contrib import admin
from social.models import Social

class SocialAdmin(admin.ModelAdmin):
    """
    Manages admin for pages
    """
    pass

admin.site.register(Social, SocialAdmin)
