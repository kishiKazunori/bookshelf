from .settings import *

DEBUG = True

ALLOWED_HOST = ['*']

DATABASES = {
    'default': {
        'ENGIE' : 'django.db.backends.postgresql',
        'NAME' : 'djangoTodoList',
        'USER': 'postgres',
        'PASSWORD':'password',
        'HOST':'db',
        'PORT': '5432'
    }
}