#!/usr/bin/env bash
set -ex

export APP_MODE=api

echo api.sh: running management tasks
python ./project/manage.py migrate
python ./project/manage.py collectstatic --noinput
python ./project/manage.py compilemessages

gunicorn \
  project.project.wsgi \
  --bind "${DJANGO_HOST:-0.0.0.0}":"${DJANGO_PORT:-5000}" \
  --chdir="$APP_HOME/project/" \
  --reload \
  --timeout 500 \
  --workers "${DJANGO_WORKERS:-4}"