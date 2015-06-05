"""frikr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'photos.views.home', name="home"),
    url(r'^login/$', 'photos.views.login', name="login"),
    url(r'^logout/$', 'photos.views.logout', name="logout"),
    url(r'^photos/(?P<pk>[0-9]+)-(.*)/$', 'photos.views.photo_detail', name="photo_detail"),
    url(r'^profile/$', 'photos.views.profile', name="profile"),
]
