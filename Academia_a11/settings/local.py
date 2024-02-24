from .base import *
import dj_database_url
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config('postgres://deus:WComgPadvQsjHQViFUw0E1qGKgbhip4R@dpg-cncpvf6g1b2c739j9jj0-a.oregon-postgres.render.com/db_academia_bhxk', conn_max_age=600)
}

STATIC_URL = '/static/'
MEDIA_URL = '/gallery/'
