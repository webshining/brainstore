from pathlib import Path

import dj_database_url
from environs import env

env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = env.bool("DEBUG", default=True)

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-k6cwxwqj#4re=!r9ayei8bdm9$yjzfo333&$26jul*jdt(lgl("

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

# Application definition
INSTALLED_APPS = [
    "jazzmin",
    "django_celery_beat",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "ai",
    "users",
    "bot",
    "reminder",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "users.middlewares.UserLanguageMiddleware",
]

ROOT_URLCONF = "app.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "app.wsgi.application"


# Database settings
DATABASE_URL = env.str("DATABASE_URL", default="sqlite:///database.sqlite3")
DATABASES = {"default": dj_database_url.config(default=DATABASE_URL)}

# Celery settings
CELERY_TIMEZONE = "UTC"
CELERY_ENABLE_UTC = True
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", default="redis://default@localhost:6379/0")
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# Auth settings
AUTH_USER_MODEL = "users.User"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Timezone
TIME_ZONE = "UTC"
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"
STATIC_ROOT = BASE_DIR.joinpath("staticfiles")
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Language settings
LANGUAGE_CODE = "en-us"
USE_I18N = True
LANGUAGES = [
    ("en", "English"),
    ("ru", "Русский"),
    ("uk", "Українська"),
]
LOCALE_PATHS = [BASE_DIR / "locale"]

# Telegram Bot settings
TELEGRAM_BOT_TOKEN = env.str("TELEGRAM_BOT_TOKEN")
GOOGLE_AI_API_KEY = env.str("GOOGLE_AI_API_KEY")
