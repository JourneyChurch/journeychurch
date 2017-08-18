from django.shortcuts import get_object_or_404, render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from media.models import Series, Experience
from utils.dates.format import format_two_dates


# Show all series
def get_all_series(request):

    # all series ordered by date
    all_series = Series.objects.all().order_by("-entry_date")

    context = {
        "all_series": all_series
    }

    return render(request, 'media/series/index.html', context)


# Show one series
def get_series(request, slug):

    # get series by slug
    series = get_object_or_404(Series, slug=slug)

    # get experiences from series ordered by date
    experiences = Experience.objects.filter(series__id=series.id).order_by("entry_date")

    # If there is one experience in series, redirect to that experience
    if experiences.count() == 1:
        return redirect('get_experience', slug=experiences[0].slug)

    # get start date and end date of series from date of first and last experience
    start_date = experiences[0].entry_date
    end_date = experiences.reverse()[0].entry_date

    # format dates into one string
    date = format_two_dates(start_date, end_date)

    context = {
        "title": series.title,
        "image": series.image.url,
        "experiences": experiences,
        "date": date
    }

    return render(request, 'media/series/details.html', context)


# Show all experiences
def get_all_experiences(request):

    # all experiences ordered by date
    experiences = Experience.objects.all().order_by("-entry_date")

    context = {
        "experiences": experiences
    }

    return render(request, 'media/experiences/index.html', context)


# Show one experience
def get_experience(request, slug):

    # get experience by slug
    experience = get_object_or_404(Experience, slug=slug)

    # Get series id
    series_id = experience.series.id

    # get other experiences from series
    other_experiences = Experience.objects.filter(series__id=series_id).exclude(id=experience.id).order_by("entry_date")

    context = {
        "experience": experience,
        "other_experiences": other_experiences
    }

    return render(request, 'media/experiences/details.html', context)


# Show one videogroup
def get_video_group(request, slug):
    return HttpResponse("Video Group %s" % slug)


# Show one video
def get_video(request, slug):
    return HttpResponse("Video %s" % slug)
