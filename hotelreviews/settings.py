

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '8fr_p^do!jp@1*0l-=1z_cjd)=j9i-@b!zp2=xml$)r_@o43w='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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




ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.sites',
    'django.contrib.admin',
    'registration',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.shortcuts',
	'bootstrap3',
    'hotelsite',
	'django_google_maps',
    )

SITE_ID = 1
ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window
REGISTRATION_AUTO_LOGIN = True # Automatically log the user in.
GOOGLE_MAPS_API_KEY =  'AIzaSyAEL9k6gS-nZw-XvmS4cCoz1k__I0NCF3g' 
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'hotelreviews.urls'

#WSGI_APPLICATION = 'hotelreviews.wsgi.application'



# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
# define your base directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
STATIC_URL = '/static/'
# define where your static files will be collected
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# keep it empty for the moment
STATICFILES_DIRS = (
)
TEMPLATE_DIRS = (os.path.join(BASE_DIR, "templates"),)
