#!/bin/sh

set -e

# Only run migrations and collectstatic for the web server
if [ $# -eq 0 ] || [ "$1" = "gunicorn" ]; then
    python manage.py collectstatic --noinput
    python manage.py migrate --noinput
fi

if [ $# -eq 0 ]; then
    exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
else
    exec "$@"
fi