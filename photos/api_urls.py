#encoding:UTF-8
from django.conf.urls import patterns, url
from photos import api

urlpatterns = patterns('',

    # api urls
    url(r'^users/$', api.UserListAPI.as_view(), name="user_list_api"),
    url(r'^users/(?P<pk>[0-9]+)/$', api.UserDetailAPI.as_view(), name="user_detail_api"),


)
