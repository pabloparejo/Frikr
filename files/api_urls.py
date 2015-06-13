#encoding:UTF-8

from django.conf.urls import patterns, url, include
from files.api import FileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'files', FileViewSet)


urlpatterns = patterns('',
    # api urls
    url(r'', include(router.urls)),
)
