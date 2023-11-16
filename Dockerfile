FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y && apt-get install python3 -y && apt-get install python3-pip -y 

WORKDIR /tp2

COPY . /tp2

RUN pip3 install -r requirements.txt

