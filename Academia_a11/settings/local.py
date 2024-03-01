from .base import *
import dj_database_url
from .env_var import RENDER_EXTERNAL_HOSTNAME

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(default=env_vars['DB_LINK'])
}


STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'
