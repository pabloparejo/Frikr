#encoding:UTF-8
"""
Django settings for frikr project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jgx$_&gz0tr_z-j!((()@6164r_$bk5jc)2cz)3mw=qq0_3v4h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'photos',
    'frikr'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'frikr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'frikr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'


# Photos App Settings

## COPYRIGHT CONSTS
APACHE = "Av2"
COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
    (APACHE, 'Apache License v2.0'),
    (COPYRIGHT, 'Copyright'),
    (COPYLEFT, 'CopyLeft'),
    (CREATIVE_COMMONS, 'Creative Commons'),
)

DEFAULT_LICENSE = CREATIVE_COMMONS

## VISIBILITY CONSTS
PUBLIC = 'PUB'
PRIVATE = "PRI"

VISIBILITY = (
    (PUBLIC, 'Public'),
    (PRIVATE, 'Private'),
)

DEFAULT_VISIBILITY = PUBLIC

# from http://goo.gl/G2nCu7
BADWORDS = (u"Abollao", u"Abrazafarolas", u"Afilasables", u"Analfabestia", u"Apollardao", u"Arrastramantas", u"Arrollapastos", u"Asaltapozos", u"Asustatrenes", u"Bailaferias", u"Bebecharcos", u"Bobolaverga", u"Bolascombro", u"Cabezabuque", u"Cabezakiko", u"Cabezantorcha", u"Cagaestacas", u"Cagaportales", u"Cansaliebres", u"Cantamañanas", u"Caracartón", u"Carachancla", u"Caraespátula", u"Caraestaca ", u"Carahogaza", u"Carajaula", u"Caranabo", u"Carapan", u"Carasapo", u"Carasuela", u"Cazurro", u"Cebollino", u"Cenutrio", u"Ceporro", u"Chafacharcos", u"Chimpamonas", u"Chupaescrotos", u"Cierrabares", u"Cuerpoescombro", u"Culoalberca", u"Descosealpargatas", u"Desbaratabailes", u"Empaellao", u"Empanao", u"Enderezaplátanos", u"Esgarramantas", u"Feodoble", u"Follacabras", u"Follácaros", u"Gilipipas", u"Huelebragas", u"Lechuguino", u"Limpiatubos", u"Mamahostias", u"Mangurrián", u"Mascachapas", u"Masturbamulos", u"Masturbaperros", u"Masturbavacas", u"Mataperros", u"Meapilas", u"Membrillo", u"Mierdaseca", u"Morroesfinge", u"Morroperca", u"Morroputa", u"Muerdealmohadas", u"Pataliebre", u"Pecholata", u"Pechopértiga ", u"Peinabombillas", u"Peinaburras", u"Pelabombillas", u"Pelagatos", u"Pelandrusca", u"Pelarrabos", u"Pellizcacristales", u"Perroflauta", u"Pinchacolillas", u"Pisapedales", u"Pudrecolchones", u"Putapénico", u"Pánfilo", u"Saltacequias", u"Sietemesino", u"Soplanucas", u"Soplasartenes", u"Tarambana", u"Tolai", u"Tontol\'lápiz", u"Tontolaba", u"Tontoligo", u"Tontoloscojones", u"Tontopolla", u"Tontoprofundo", u"Tragaldabas", u"Tragalpacas", u"Tuercebotas", u"Vuelcalitros", u"Zanahorio", u"Zarandajo", u"Zarrapastroso", u"Zopenco", u"Zurremierdas", )

REST_FRAMEWORK = {
    "PAGINATE_BY": 3,
    "PAGINATE_BY_PARAM": "page_size",
    "MAX_PAGINATE_BY": 100
}