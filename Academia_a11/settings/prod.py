from .base import *
import dj_database_url
from os import path

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_vars['DEBUG']

<<<<<<< HEAD
ALLOWED_HOSTS = env_vars['ALLOWED_HOSTS']
=======
ALLOWED_HOSTS = [
"44.226.145.213",
"54.187.200.255",
"34.213.214.55",
"35.164.95.156",
"44.230.95.183",
"44.229.200.200"
]
>>>>>>> 03d23f0c163c935a1f51f1f92fe751cda3ea2827



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

DATABASES['default'] = dj_database_url.parse(env_vars['DB_LINK'])


# DATABASES["default"] = dj_database_url.parse("postgres://deus:OrZmSVTxLKcHl24DbgBd7cURmvpcSHFh@dpg-cncj1qen7f5s73bh31ug-a.oregon-postgres.render.com/db_academia")


STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'



if not DEBUG:
    # Tell Django to copy static assets into a path called `staticfiles` (this is specific to Render)
    STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')
    # Enable the WhiteNoise storage backend, which compresses static files to reduce disk use
    # and renames the files with unique names for each version to support long-term caching
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'














    #############




ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'
