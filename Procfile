release: chmod u+x app/release.sh && ./app/release.sh
web: gunicorn --chdir app wsgi:application --log-file - --log-level debug