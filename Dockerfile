FROM ubuntu:latest

RUN apt-get update && apt-get upgrade -y && apt-get install python3 -y && apt-get install python3-pip -y 

WORKDIR /tp2

COPY . /tp2

RUN pip3 install -r requirements2.txt

RUN apt-get install -y libgl1-mesa-glx
RUN apt-get install -y libglib2.0-0


