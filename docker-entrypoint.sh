#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --no-input

# Apply database migrations if any
echo "Apply database migrations"
# python manage.py migrate

# Start server
echo "Starting gunicorn server"
echo "env variable:- $ENV"
if [ "$ENV" == "prod" ]; then
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn --preload -c python:settings.gunicorn rentdoor.wsgi
else
    gunicorn --preload -c python:settings.gunicorn rentdoor.wsgi
fi

