#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic

# Apply database migrations if any
echo "Apply database migrations"
# python manage.py migrate

# Start server
echo "Starting gunicorn server"
gunicorn --preload -c python:settings.gunicorn rentdoor.wsgi
