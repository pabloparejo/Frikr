#encoding:utf-8
from django.contrib.auth.models import User

from django.db import models
# Create your models here.


class Photo(models.Model):
    ## COPYRIGHT CONSTS
    COPYRIGHT = 'RIG'
    COPYLEFT = 'LEF'
    CREATIVE_COMMONS = 'CC'

    LICENSES = (
        (COPYRIGHT, 'Copyright'),
        (COPYLEFT, 'CopyLeft'),
        (CREATIVE_COMMONS, 'Creative Commons'),
    )

    ## VISIBILITY CONSTS
    PUBLIC = 'PUB'
    PRIVATE = "PRI"

    VISIBILITY = (
        (PUBLIC, 'Public'),
        (PRIVATE, 'Private'),
    )

    owner = models.ForeignKey(User)

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)    # Sets datetime automatically when created
    modified_on = models.DateTimeField(auto_now=True)       # Sets datetime automatically when it is saved
    license = models.CharField(max_length=3, choices=LICENSES, default=CREATIVE_COMMONS)
    visibility = models.CharField(max_length=3, choices=VISIBILITY, default=PUBLIC)

    def __unicode__(self):
        return self.name