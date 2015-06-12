#encoding:UTF-8
from django.conf import settings
from django.core.exceptions import ValidationError

BADWORDS = getattr(settings, 'BADWORDS', [])
def badwords(value):
    for badword in BADWORDS:
        if badword.lower() in value.lower():
            raise ValidationError(badword + u" IS NOT ALLOWED")

    return True