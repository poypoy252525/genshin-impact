#!/bin/sh

set -e

python manage.py collectstatic --noinput
python manage.py migrate --noinput

if [ $# -eq 0 ]; then
    exec gunicorn config.wsgi:application --bind 0.0.0.0:8000
else
    exec "$@"
fi