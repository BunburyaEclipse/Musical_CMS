from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": database_data['NAME'],
        "USER": database_data['USER'],
        "HOST": database_data['HOST'],
        "PASSWORD": database_data['PASSWORD'],
        "PORT": database_data['PORT'],
    }
}


STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'
