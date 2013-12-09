# -*- coding: utf-8 -*-
DEBUG = True

SECRET_KEY = "jqx$20k4d^_c7zq9=m1dyuv-f_izs1r^s6pug=vdtwpq-b7o79"

DATABASES = {
    "default": {
        # Ends with "postgresql_psycopg2", "mysql", "sqlite3" or "oracle".
        "ENGINE": "django.db.backends.sqlite3",
        # DB name or path to database file if using sqlite3.
        "NAME": "dev.db",
        # Not used with sqlite3.
        "USER": "",
        # Not used with sqlite3.
        "PASSWORD": "",
        # Set to empty string for localhost. Not used with sqlite3.
        "HOST": "",
        # Set to empty string for default. Not used with sqlite3.
        "PORT": "",
    }
}

ALLOWED_HOSTS=['*']

#SEARCH_MODEL_CHOICES="pages.Page main.Link"

ACCOUNTS_PROFILE_FORM_EXCLUDE_FIELDS = (
    "email",
    "first_name",
    "last_name",
    'website',
    'bio',
)

USE_I18N = True
LANGUAGE_CODE = 'zh'

#排除