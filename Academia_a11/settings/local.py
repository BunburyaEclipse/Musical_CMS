from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": database_env['db_name'],
        "USER": database_env['db_user'],
        "HOST": database_env['db_host'],
        "PASSWORD": database_env['db_passwd'],
        "PORT": database_env['db_port'],
    }
}


STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'
