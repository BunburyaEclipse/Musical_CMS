from .base import *
import dj_database_url
from os import path
from .env_var import RENDER_EXTERNAL_HOSTNAME

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": dj_database_url.config(default=env_vars['DB_LINK'])
}



# DATABASES["default"] = dj_database_url.parse("postgres://deus:OrZmSVTxLKcHl24DbgBd7cURmvpcSHFh@dpg-cncj1qen7f5s73bh31ug-a.oregon-postgres.render.com/db_academia")


STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'



STORAGES = {
    # ...
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


STATIC_ROOT = path.join(BASE_DIR, 'staticfiles')



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases


STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'



##### CONFIGURACIÓNES DE SEGURIDAD


# SECURE_SSL_REDIRECT = True

# SESSION_COOKIE_SECURE = True

# CSRF_COOKIE_SECURE = True

# SECURE_HSTS_SECONDS = 31536000  # Un año en segundos

# SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# SECURE_HSTS_PRELOAD = True