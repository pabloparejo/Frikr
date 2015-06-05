#encoding:utf-8
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect

from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from photos.forms import LoginForm

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

@login_required(login_url="login")
def profile(request):
    context = {
        "photos": request.user.photo_set.all()
    }

    return render(request, "photos/profile.html", context)

def login(request):
    form = LoginForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                django_login(request, user)
                url = request.GET.get('next', 'profile')
                return redirect(url)
            else:
                context["errors"] = 'Su usuario no está activo'
        else:
            context["errors"] = 'Usuario o contraseña incorrectos'

    return render(request, "photos/login.html", context)

def logout(request):
    if request.user.is_authenticated():
        django_logout(request)

    return redirect("home")