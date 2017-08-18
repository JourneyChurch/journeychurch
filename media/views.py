from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from media.models import Series, Experience
from utils.dates.format import format_two_dates

# Show all series
def get_all_series(request):
    return HttpResponse("All Series")

# Show one series
def get_series(request, slug):

    # get series by slug
    series = get_object_or_404(Series, slug=slug)

    # get experiences from series ordered by date
    experiences = Experience.objects.filter(series__id=series.id).order_by("entry_date")

    # get start date and end date of series from date of first and last experience
    start_date = experiences[0].entry_date
    end_date = experiences.reverse()[0].entry_date

    date = format_two_dates(start_date, end_date)

    context = {
        "title": series.title,
        "image": series.image.url,
        "experiences": experiences,
        "date": date
    }

    return render(request, 'media/series.html', context)

# Show one experience
def get_experience(request, slug):
    return HttpResponse("Experience %s" % slug)

# Show one videogroup
def get_video_group(request, slug):
    return HttpResponse("Video Group %s" % slug)

# Show one video
def get_video(request, slug):
    return HttpResponse("Video %s" % slug)
