from .settings import *


DEBUG = False

CELERY_BROKER_URL = ''

CELERY_RESULT_BACKEND = ''

ALLOWED_HOSTS = ['thumbnailer-django.herokuapp.com']

BROKER_URL = os.environ['REDIS_URL']

CELERY_RESULT_BACKEND = os.environ['REDIS_URL'