FROM python:3.8.6-buster

RUN apt update
RUN apt-get install cron -y
RUN alias py=python

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./app .
COPY ./requirements.txt /usr/src/app

RUN pip install -r requirements.txt

# cron options
RUN mkdir /cron
RUN touch /cron/django_cron.log

EXPOSE 8000

CMD service cron start && python manage.py runserver 0.0.0.0:8000