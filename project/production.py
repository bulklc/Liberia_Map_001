from project.settings import *


DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'liberia',
        'USER': os.environ.get('POSTGRES_DB_USER'),
        'PASSWORD': os.environ.get('POSTGRES_DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

