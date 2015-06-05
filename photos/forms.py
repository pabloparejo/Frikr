#encoding:UTF-8
from django import forms
from models import Photo

class LoginForm(forms.Form):
    username = forms.CharField(label="Usuario")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)


class PhotoFrom(forms.ModelForm):
    class Meta:
        model = Photo
        exclude = ("owner",)