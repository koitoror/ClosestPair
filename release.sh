# !/bin/sh

set -e

ls -la /app/frontend/staticfiles/
ls -la /app/frontend/build

whoami

echo "Running Release Tasks"

# python manage.py wait_for_db
# python manage.py collectstatic --noinput

echo "Running Database migrations and migrating the new changes"
# python manage.py makemigrations

python manage.py migrate --plan
python manage.py migrate --noinput

echo "Running Server"
# python manage.py runserver 0.0.0.0:8000
# uwsgi --socket :8000 --workers 4 --master --enable-threads --module app.wsgi
# gunicorn --chdir backend app.wsgi
# gunicorn app.wsgi:application --bind 0.0.0.0:8000

echo "Done.."