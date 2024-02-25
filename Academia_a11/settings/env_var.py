import os
import environ

env = environ.Env()
environ.Env.read_env()

ENVIROMENT = env

RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')