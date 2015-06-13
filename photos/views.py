#encoding:utf-8
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse

from django.contrib.auth import logout as django_logout, login as django_login, authenticate
from django.utils.decorators import method_decorator
from photos.forms import LoginForm, PhotoFrom

from django.views.generic import View, ListView

from photos.models import Photo
from frikr.settings import PUBLIC # this is not a good idea!
# Create your views here.
from photos.views_queryset import PhotoQueryset


class HomeView(View):
    def get(self, request):
        photos = Photo.objects.filter(visibility=PUBLIC).order_by("-created_on")
        context = {"photos": photos[:5]} # This is actually optimal
        return render(request, "photos/home.html", context)



class AddPhotoView(View):

    @method_decorator(login_required(login_url="login"))
    def get(self, request):
        message = None
        form = PhotoFrom()
        context = {
            "form": form,
            "message": message
        }
        return render(request, "photos/add_photo.html", context)

    @method_decorator(login_required(login_url="login"))
    def post(self, request):
        message = None
        photo = Photo(owner=request.user)
        form = PhotoFrom(request.POST, instance=photo)
        if form.is_valid():
            new_photo = form.save()
            photo_url = reverse("photo_detail", args=[new_photo.pk, new_photo.name])
            message = "Photo saved! <a href='{0}'>View</a>".format(photo_url)
            form = PhotoFrom()

        context = {
            "form": form,
            "message": message
        }
        return render(request, "photos/add_photo.html", context)

class PhotoDetailView(View):

    def get(self, request, pk):

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

class ProfileView(View):
    @method_decorator(login_required(login_url="login"))
    def get(self, request):
        context = {
            "photos": request.user.photo_set.all()
        }

        return render(request, "photos/profile.html", context)



class LogoutView(View):
    def get(self, request):
        if request.user.is_authenticated():
            django_logout(request)

        return redirect("home")


class LoginView(View):

    def get(self, request):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "photos/login.html", context)

    def post(self, request):
        form = LoginForm(request.POST)
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

class PhotoList(PhotoQueryset, ListView):
    model = Photo