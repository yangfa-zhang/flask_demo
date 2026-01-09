#!/bin/sh
set -e

echo "Starting gunicorn with gevent workers..."

exec gunicorn \
    -w 2 \
    -k gevent \
    -b 0.0.0.0:5001 \
    app:app
