#!/bin/bash

# Collect static files
echo "Collect static files"
"yes" | python manage.py collectstatic

# Apply database migrations if any
echo "Apply database migrations"
# python manage.py migrate

# Start server
echo "Starting gunicorn server"
echo "env variable:- $ENV"

sed -i 's/new_relic_license_key/'$NEW_RELIC_LICENSE_KEY'/g' newrelic.ini

if [ "$ENV" == "prod" ]; then
    NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn --preload -c python:settings.gunicorn rentdoor.wsgi
else
    gunicorn --preload -c python:settings.gunicorn rentdoor.wsgi
fi

