import os

from django.conf.global_settings import CACHES

from .base import *

DEBUG = False

ADMINS = [
    ('samuel', 'samuelosondu99@gmail.com'),
]

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': os.environ.get('POSTGRES_DB'),
    'USER': os.environ.get('POSTGRES_USER'),
    'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
    'HOST': 'db',
    'PORT': 5432,

    }
}


REDIS_URL = 'redis://cache:6379'
CACHES['default']['LOCATION'] = REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts'] = [REDIS_URL]

