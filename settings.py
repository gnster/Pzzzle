# -*- coding: utf-8 -*-
# Django settings for pzzzle project.

import os
from datetime import timedelta

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Glader', 'glader.ru@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'pzzzle',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Asia/Yekaterinburg'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = False

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/"
PROJECT_PATH = os.path.dirname(__file__)
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'gctmlun6)&t)ex7yp^!$)e$cr!8-8-!h4-9&mg^@nnigg!pg_l'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'pzzzle.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django_errorlog',

    'south',

    'core',
)

FORCE_SCRIPT_NAME = ""

TABLE = (30, 5)
THUMBNAIL_SIZE = (100, 100)
THUMBNAIL_PATH = os.path.join(MEDIA_ROOT, 'data')
LOCK_PERIOD = timedelta(minutes=10)

LOG_PATH = '/var/log/projects/pzzzle'

EXCEPTION_LOG_FILE = os.path.join(LOG_PATH, 'exception.log')
TRACEBACK_LOG_FILE = os.path.join(LOG_PATH, 'traceback.log')

LOGGING_FORMAT = '%(asctime)s %(name)-15s %(levelname)s %(message)s'
LOGGING_MAX_FILE_SIZE = 1 * 1024 * 1024 #: Максимальный размер файла с логами в байтах.
LOGGING_MAX_FILES_COUNT = 10 #: Количество бекапов файлов с логами.

CACHE_ROOT = 'pzzzle/'
CACHE_BACKEND = 'locmem:///'

try:
    from local_settings import *
except ImportError:
    pass