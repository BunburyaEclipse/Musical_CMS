from .base import *
import dj_database_url
from os import path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_vars['DEBUG']

ALLOWED_HOSTS = env_vars['ALLOWED_HOSTS']


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

DATABASES['default'] = dj_database_url.parse(env_vars['DB_LINK'])


# DATABASES["default"] = dj_database_url.parse("postgres://deus:OrZmSVTxLKcHl24DbgBd7cURmvpcSHFh@dpg-cncj1qen7f5s73bh31ug-a.oregon-postgres.render.com/db_academia")


STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'



STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'














    #############




ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'
