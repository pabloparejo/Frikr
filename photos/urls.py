#encoding:UTF-8
from django.conf.urls import patterns, url
from photos import views

urlpatterns = patterns('',
    # web urls

    url(r'^$', views.HomeView.as_view(), name="home"),
    url(r'^photos/$', views.PhotoList.as_view(), name="photo_list"),
    url(r'^photos/(?P<pk>[0-9]+)-(.*)/$', views.PhotoDetailView.as_view(), name="photo_detail"),
    url(r'^add_photo/$', views.AddPhotoView.as_view(), name="add_photo"),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/$', views.LogoutView.as_view(), name="logout"),
    url(r'^profile/$', views.ProfileView.as_view(), name="profile"),

)
