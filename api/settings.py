import os
from django.conf import settings
import api

ALLOWED_HOSTS = (
    'angular-django',
    '127.0.0.1',
    'localhost',
    'angular-django:8080',
    'angular-django:8000',
    'localhost:8000',
    '127.0.0.1:8000',
    '127.0.0.1:8080'

)
CORS_ORIGIN_ALLOW_ALL = False

CORS_ORIGIN_WHITELIST = (
    #'google.com',
    #'hostname.example.com',
    'angular-django:8080',
    'angular-django:8000',
    'localhost:8000',
    '127.0.0.1:8000',
    '127.0.0.1:8080'
)

CORS_ALLOW_METHODS = (
    #'DELETE',
    'GET',
    #'OPTIONS',
    #'PATCH',
    'POST',
    #'PUT',
)

CORS_ALLOW_HEADERS = (
    #'accept',
    #'accept-encoding',
    'authorization',
    'content-type',
    #'dnt',
    #'origin',
    #'user-agent',
    'x-csrftoken',
    #'x-requested-with',
    #'Access-Control-Allow-Credentials'
)
CORS_ALLOW_CREDENTIALS = True

settings.TEMPLATES.append(
    {
        'NAME': 'api',
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.dirname(api.__file__) + '/static/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
)