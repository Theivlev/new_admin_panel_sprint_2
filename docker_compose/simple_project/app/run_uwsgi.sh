#!/usr/bin/env bash

set -e

python manage.py migrate

python manage.py collectstatic --noinput

chown www-data:www-data /var/log

uwsgi --strict --ini /etc/app/uwsgi.ini
