from django.shortcuts import render
from django.http import HttpResponse

# Show all series
def get_all_series(request):
    return HttpResponse("All Series")

# Show one series
def get_series(request, slug):
    return HttpResponse("Series %s" % slug)

# Show one experience
def get_experience(request, slug):
    return HttpResponse("Experience %s" % slug)

# Show one videogroup
def get_video_group(request, slug):
    return HttpResponse("Video Group %s" % slug)

# Show one video
def get_video(request, slug):
    return HttpResponse("Video %s" % slug)
