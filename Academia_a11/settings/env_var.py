import os
import environ

env = environ.Env()
environ.Env.read_env()

ENVIROMENT = env

database_env = {
    "db_name": os.environ.get('NAME'),
    "db_user": os.environ.get('USER'),
    "db_passwd": os.environ.get('PASSWORD'),
    "db_host": os.environ.get('HOST'),
    "db_port": os.environ.get('PORT'),
    "SECRET_KEY": os.environ.get('DJANGO_SECRET_KEY'),
    "db_link": os.environ.get('DB_LINK')
    # "allowed_hosts": os.environ('ALLOWED_HOSTS').split(" ")
}