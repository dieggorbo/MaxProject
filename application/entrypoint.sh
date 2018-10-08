#!/bin/sh

set -e

#export GUNICORN_CMD_ARGS="--name APP --bind 0.0.0.0:443 --chdir /srv/www/application --pid /var/run/gunicorn.pid --disable-redirect-access-to-syslog --capture-output --access-logfile /var/log/gunicorn/application-access.log --error-logfile /var/log/gunicorn/application-error.log --keyfile /etc/ssl/certs/dummy-cert.crt --certfile /etc/ssl/certs/dummy-cert.crt"
export GUNICORN_CMD_ARGS="--name APP --bind 0.0.0.0:443 --chdir /srv/www/application --pid /var/run/gunicorn.pid --keyfile /etc/ssl/certs/dummy-cert.crt --certfile /etc/ssl/certs/dummy-cert.crt"
source /srv/www/environment/bin/activate

export GUNICORN_CMD_ARGS="${GUNICORN_CMD_ARGS} --worker-class gevent --reload --workers $[(2*$(nproc))+1] --backlog 2048 --worker-connections 500 --keep-alive 30";

gunicorn wsgi:app
