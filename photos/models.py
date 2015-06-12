#encoding:utf-8
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models
# Create your models here.
from photos.validators import badwords

LICENSES = getattr(settings, 'LICENSES', ())
DEFAULT_LICENSES = getattr(settings, 'DEFAULT_LICENSES', ())

VISIBILITY = getattr(settings, 'VISIBILITY', ())
DEFAULT_VISIBILITY = getattr(settings, 'DEFAULT_VISIBILITY', ())

class Photo(models.Model):

    owner = models.ForeignKey(User)

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True, validators=(badwords,))
    created_on = models.DateTimeField(auto_now_add=True)    # Sets datetime automatically when created
    modified_on = models.DateTimeField(auto_now=True)       # Sets datetime automatically when it is saved
    license = models.CharField(max_length=3, choices=LICENSES, default=DEFAULT_LICENSES)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=DEFAULT_VISIBILITY)

    def __unicode__(self):
        return self.name