FROM python:3.9-alpine3.18
LABEL mantainer="koitoror"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Get app
# RUN python -m django --version
# RUN python -m django startproject app /app
# RUN python -m django startapp closest /closest
# RUN python manage.py createsuperuser --email admin@example.com --username admin


COPY ./app /app/app/
COPY ./closest app/closest
COPY ./requirements.txt /app/
COPY ./manage.py /app/
COPY ./entrypoint.sh /app/

WORKDIR /app

RUN pip install -r requirements.txt
 
EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000", "--settings=app.settings" ]
CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "app.wsgi:application"]

