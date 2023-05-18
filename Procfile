# release: chmod u+x ./release.sh && ./release.sh
web: gunicorn --chdir app wsgi:application --log-file - --log-level debug