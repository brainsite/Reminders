import os
from pathlib import Path

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = Path(__file__).resolve().parent.parent


ALLOWED_HOSTS = ['*']

SECRET_KEY = 'kg4+$_+3hs0t_(0bxq^xm+wc9z4z1ksd5r-1*-kvl&=g33g*hf'



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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
]

DEFAULT_FROM_EMAIL = 'rent@brainsite.ru'
EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_PASSWORD = 'RentaCar123'
EMAIL_HOST_USER = 'rent@brainsite.ru'
EMAIL_PORT = '465'
EMAIL_USE_SSL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'remind',
        'USER': 'django',
        'PASSWORD': '4343jw8s0F4',
        'HOST': 'localhost',
    }
}


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')