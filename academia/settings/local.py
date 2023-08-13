from .base import *

#### APLICACIONES Y MIDDLEWARES DE DESARROLLO Y EXTRAS

DEVELOMEPT_APPS = [
    'django_browser_reload',
]

DEVELOMEPT_MIDDLEWARES = [
    "django_browser_reload.middleware.BrowserReloadMiddleware",
]

INSTALLED_APPS.extend(DEVELOMEPT_APPS)
MIDDLEWARE.extend(DEVELOMEPT_MIDDLEWARES)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

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
