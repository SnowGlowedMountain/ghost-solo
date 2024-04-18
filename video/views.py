from django.shortcuts import render
from django.http import Http404
from django.core.exceptions import MultipleObjectsReturned
from .models import Video

# Specific videos
def video(request, slug):
    try:
        video = Video.objects.get(slug=slug)
    except Video.DoesNotExist:
        raise Http404("Video does not exist")
    except MultipleObjectsReturned:
        video = Video.objects.filter(slug=slug).first()

    return render(request, 'pages/video.html', {'video': video})


# List of filtered videos
def videos(request):
    videos = Video.objects.all().order_by('order')
        
    return render(request, 'pages/videos.html', {'videos': videos})
