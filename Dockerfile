FROM python:3.8.6-buster

RUN apt update
RUN alias py=python

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY ./app .
COPY ./requirements.txt /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python manage.py runserver 0.0.0.0:8000