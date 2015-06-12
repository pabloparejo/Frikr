#encoding:UTF-8
from django import forms
from models import Photo

from django.conf import settings

BADWORDS = getattr(settings, 'BADWORDS', [])

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class PhotoFrom(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ("owner",)

    def clean(self):
        cleaned_data = super(PhotoFrom, self).clean()
        description = cleaned_data.get('description', '')
        for badword in BADWORDS:
            if badword.lower() in description.lower():
                raise forms.ValidationError(badword + u" IS NOT ALLOWED")

        return cleaned_data