from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = [
    "housedoor.in",
    "localhost",
    "127.0.0.1",
    "https://housedoor.in",
    "139.59.17.7",
]

CSRF_TRUSTED_ORIGINS = ["https://housedoor.in"]

MEDIA_FILE_PREFIX = "https://housedoor.in"
