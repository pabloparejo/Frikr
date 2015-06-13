#encoding:UTF-8
from django.conf.urls import patterns, url, include
from photos import api
from photos.api import PhotoViewSet, UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'photos', PhotoViewSet)
router.register(r'users', UserViewSet, base_name="user")


urlpatterns = patterns('',
    # api urls
    url(r'', include(router.urls)),

)
