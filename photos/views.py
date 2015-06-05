#encoding:utf-8
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth import logout as django_logout, login as django_login, authenticate

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


def login(request):
    context = {}
    if request.method.upper() == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                django_login(request, user)
                return redirect("home")
            else:
                context["errors"] = 'Su usuario no está activo'
        else:
            context["errors"] = 'Usuario o contraseña incorrectos'

    return render(request, "photos/login.html", context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)

    return redirect("/")