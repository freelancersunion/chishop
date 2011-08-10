import os
import chishop
from chishop.conf.default import *

DEBUG = True
TEMPLATE_DEBUG = True

TIME_ZONE = 'America/New_York'

DATABASES = dict(
	default = dict(
		ENGINE = 'django.db.backends.postgresql_psycopg2',
		NAME = 'chishop',
		USER = 'chishop',
		PASSWORD = 'GogDadjerm1',
		HOST = '',
		PORT = '',
	)
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.RemoteUserMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.RemoteUserBackend',
)

HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_SITECONF = 'chishop.search_sites'
HAYSTACK_WHOOSH_PATH = os.path.join(os.path.dirname(chishop.__file__), 'haystack')
DJANGOPYPI_PROXY_MISSING = True
