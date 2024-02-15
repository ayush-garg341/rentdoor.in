from .base import *


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "debug_toolbar",
    "debug_panel",
    "rest_framework",
    "reviews",
    "app_users",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = [  # <-- NEW
    "127.0.0.1",  # <-- NEW
]  # <-- NEW


def show_toolbar(request):  # <-- NEW
    return True  # <-- NEW


DEBUG_TOOLBAR_CONFIG = {  # <-- NEW
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,  # <-- NEW
}
