FROM python:3.9-alpine3.18
LABEL mantainer="koitoror"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
COPY ./requirements.txt /app/requirements.txt

# Get app
# RUN python -m django --version
# RUN python -m django startproject app /app
# RUN python -m django startapp closest /closest
# RUN python manage.py createsuperuser --email admin@example.com --username admin


COPY ./app /app
COPY ./closest /closest
WORKDIR /app
EXPOSE 8000

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=app.settings" ]
