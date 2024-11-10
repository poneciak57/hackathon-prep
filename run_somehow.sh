#!/bin/sh



# DO NOT CHANGE ANYTHING

set -e

host="db"

until nc -z "$host" 5432; do
  echo "Waiting for $host:5432..."
  sleep 1
done

echo "$host is up - executing command"
python manage.py migrate
python manage.py runserver 0.0.0.0:8000