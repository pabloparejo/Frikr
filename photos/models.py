#encoding:utf-8

from django.db import models

# Create your models here.


class Photo(models.Model):
    COPYRIGHT = 'RIG'
    COPYLEFT = 'LEF'
    CREATIVE_COMMONS = 'CC'

    LICENSES = (
        (COPYRIGHT, 'Copyright'),
        (COPYLEFT, 'CopyLeft'),
        (CREATIVE_COMMONS, 'Creative Commons'),
    )

    name = models.CharField(max_length=150)
    url = models.URLField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # Sets datetime automatically when created
    modified_on = models.DateTimeField(auto_now=True) # Sets datetime automatically when it is saved
    license = models.CharField(max_length=3, choices=LICENSES)
