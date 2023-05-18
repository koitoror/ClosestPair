#!/bin/bash

set -x;

/bin/bash /entrypoint.sh mysqld > /dev/null 2>&1 &

echo "Waiting for MySQL"
until echo '\q' | mysql -h"$_HOST" -P"$_PORT" -uroot -p"$_ROOT_PASSWORD" $_DATABASE; do
    >&2 echo "MySQL is unavailable - Sleeping..."
    sleep 2
done

echo -e "\nMySQL ready!"

python manage.py migrate
python manage.py runserver 0.0.0.0:80
