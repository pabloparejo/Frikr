#encoding:UTF-8
from django.db.models import Q
from frikr.settings import PUBLIC
from photos.models import Photo


class PhotoQueryset(object):

    def get_queryset(self):
        user = self.request.user

        if user.is_anonymous():
            return Photo.objects.filter(visibility=PUBLIC)
        elif user.is_staff:
            return Photo.objects.all()
        else:
            return Photo.objects.filter(Q(owner=user) | Q(visibility=PUBLIC))

        return super(PhotoList, list).get_queryset()
