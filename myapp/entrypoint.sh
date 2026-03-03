#!/bin/sh

echo "Waiting for Postgres..."

while ! nc -z db $POSTGRES_PORT; do
  sleep 0.5
done

echo "Postgres is up!"

python manage.py migrate
python manage.py loaddata fixtures/goods/categories.json
python manage.py loaddata fixtures/goods/products.json

exec "$@"