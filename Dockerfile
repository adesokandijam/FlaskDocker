FROM python:3.9.5-slim-buster

WORKDIR /app

COPY ./requirements.txt .
RUN apt-get update
RUN apt-get install libpq-dev gcc python-dev -y
RUN pip3 install -r requirements.txt
COPY ./app .
