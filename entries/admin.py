from django.contrib import admin
from entries.models import Entry

class EntryAdmin(admin.ModelAdmin):
    """
    Manages admin for all entries
    """

    # Prepopulates slug field from title
    prepopulated_fields = {'slug': ('title',)}

    # Organizes all entry fields into fieldset to distinguish entry fields from sepcific model fields
    fieldset = ('Entry Fields', {
            'fields': ('title', 'slug', 'entry_date', 'expiration_date')
    },)
