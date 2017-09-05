from django import template
from django.shortcuts import get_object_or_404
from pages.models import Content
from media.models import Video, Series

register = template.Library()

# Series Section:
# Custom Tag that can be accessed by {% series %}. Creates fields for a series type section
@register.inclusion_tag("pages/sections/series.html")
def series(section):

    if section.display_title:
        section_title = section.display_title
    else:
        section_title = section.title

    # Assume these are empty first
    video_title = None
    video_description = None
    youtube_id = None
    speaker = None

    # type of series
    series_type = section.series_type

    # latest series of type
    latest_series = Series.objects.filter(series_type=series_type).order_by("-entry_date").first()


    # latest experience from series
    if latest_series:
        latest_experience = latest_series.experience_set.order_by("-entry_date").first()
    else:
        latest_experience = None


    # latest experience video
    if latest_experience:
        video_id = latest_experience.video.id
        speaker = latest_experience.speaker

        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            video = None
    else:
        video = None


    # If video is public and exists
    if video:

        # Check for display title
        if video.display_title:
            video_title = video.display_title
        else:
            video_title = video.title

        video_description = video.description
        youtube_id = video.youtube_id
    else:
        video_title = None
        video_descrption = None
        youtube_id = None


    context = {
        "title": section_title,
        "slug": section.slug,
        "background_image": section.background_image,
        "background_color": section.background_color,
        "video": video,
        "video_title": video_title,
        "video_description": video_description,
        "youtube_id": youtube_id,
        "series": latest_series,
        "speaker": speaker
    }

    return context
