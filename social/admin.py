from django.contrib import admin
from entries.admin import EntryAdmin
from social.models import Social

admin.site.register(Social, EntryAdmin)
