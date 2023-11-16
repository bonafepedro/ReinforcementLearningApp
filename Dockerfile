FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y && apt-get install python3 -y && apt-get install python3-pip -y 

RUN mkdir /tp2

COPY tp2 /tp2 

WORKDIR /tp2

COPY requirements.txt /app

RUN pip3 install -r requirements.txt