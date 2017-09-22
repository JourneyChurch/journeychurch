from django.contrib import admin
from entries.admin import EntryAdmin
from careers.models import Career

class CareerAdmin(EntryAdmin):
    """
    Manages admin for careers
    """

    # Put specific fields in field set
    fieldsets = (
        EntryAdmin.fieldset,
        ('Career Fields', {
            'fields': ('summary', 'description', 'contact_name', 'contact_email')
        },)
    )

    # Show all objects in admin
    def get_queryset(self, request):
         return Career.all_objects.get_queryset()


admin.site.register(Career, CareerAdmin)
