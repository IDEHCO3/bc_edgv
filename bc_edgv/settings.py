"""
Django settings for bc_edgv project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_ROOT = os.path.join(BASE_DIR, "static_root/")
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c(389qsh!zp=boq_^3#y-)^cbyq$t2ts=h#tu3^-tns-)6o+a8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'rest_framework',
    'rest_framework_gis',
    'corsheaders',
    'bcim',
    'context_api',
    'hydra',
)

MIDDLEWARE_CLASSES = (
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


ROOT_URLCONF = 'bc_edgv.urls'

CORS_ORIGIN_ALLOW_ALL = True


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

WSGI_APPLICATION = 'bc_edgv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases


if not 'IP_SGBD' in os.environ:
    os.environ['IP_SGBD'] = '172.17.0.2'

if not 'PORT_SGBD' in os.environ:
    os.environ['PORT_SGBD'] = '5432'

if not 'DB_NAME' in os.environ:
    os.environ['DB_NAME'] = 'idehco3'

if not 'DB_USERNAME' in os.environ:
    os.environ['DB_USERNAME'] = 'idehco3'

if not 'DB_PASSWORD' in os.environ:
    os.environ['DB_PASSWORD'] = 'idehco3'

ip_sgbd = os.environ['IP_SGBD']
port_sgbd = os.environ['PORT_SGBD']
db_name = os.environ['DB_NAME']
user = os.environ['DB_USERNAME']
password = os.environ['DB_PASSWORD']

DATABASES = {
   'default': {
       'ENGINE': 'django.contrib.gis.db.backends.postgis',
       'OPTIONS': {
               'options': '-c search_path=public,bcim,idehco3,anp',

       },

       'HOST': ip_sgbd,
       'PORT': port_sgbd,
       'NAME': db_name,
       'USER': user,
       'PASSWORD': password,
   }
}

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/idehco3/bcedgv/static/'

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',)
}