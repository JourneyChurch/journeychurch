from django import template
from django.shortcuts import get_object_or_404
from pages.models import NavigationMenu

register = template.Library()

# Content:
# Custom Tag that can be accessed by {{ content }}. Extracts sections from content and gives it to content template
@register.inclusion_tag("pages/content.html")
def content(sections):
    sections_out = []

    # Loop through each section and find the section type
    for section in sections:
        if section.section_type() == "default":
            sections_out.append({
                "object": section.sectiondefault,
                "type": "default"
            })
        elif section.section_type() == "twocolumn":
            sections_out.append({
                "object": section.sectiontwocolumn,
                "type": "twocolumn"
            })
        elif section.section_type() == "threecolumn":
            sections_out.append({
                "object": section.sectionthreecolumn,
                "type": "threecolumn"
            })

    # Return list of dictionaries with type and section object.
    # Django templates use section.type to reference section["type"] on dictionaries
    return {"sections": sections_out}
