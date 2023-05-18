FROM python:3.9-alpine3.18
LABEL mantainer="koitoror"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
COPY ./requirements.txt /app/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000
