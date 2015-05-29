from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from photos.models import Photo
from frikr.settings import PUBLIC # this is not a good idea!
# Create your views here.


def home(request):
    photos = Photo.objects.filter(visibility=PUBLIC).order_by("-created_on")
    context = {"photos": photos[:5]} # This is actually optimal
    return render(request, "photos/home.html", context)

def photo_detail(request, pk):

    """possible_photos = Photo.objects.filter(pk=pk)

    if len(possible_photos) > 0:
        photo  = possible_photos[0]
        context = {
            'photo': photo
        }
        return render(....)
    else
        return HttpResponseNotFound('Ooops! photo not found')

    """

    try:
        photo = Photo.objects.get(pk=pk)
        context = {
            'photo': photo
        }
        return render(request, 'photos/photo_detail.html', context)
    except Photo.DoesNotExist:
        return HttpResponseNotFound('Ooops! photo not found')
