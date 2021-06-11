# syntax=docker/dockerfile:1
FROM python:3.8-slim

WORKDIR /app

RUN apt-get update
RUN apt-get install python3-dev default-libmysqlclient-dev gcc  -y

RUN pip3 install mysqlclient
RUN pip3 install mysql-connector-python

COPY ./src .

# Add docker-compose-wait tool -------------------
ENV WAIT_VERSION 2.7.2
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/$WAIT_VERSION/wait /wait
RUN chmod +x /wait

# CMD [ "python3", "./app.py"]