release: chmod u+x app/release.sh && ./release.sh
web: gunicorn --chdir app wsgi:application --log-file - --log-level debug