FROM ubuntu:16.04

MAINTAINER Yakup Görür "yakup.gorur@gmail.com"

COPY ./requirements.txt /HateSpeechApp/requirements.txt

WORKDIR /HateSpeechApp

RUN apt-get update -y \
    && apt-get -y install python3 \
    && apt-get -y install python3-pip
RUN pip3 install -r requirements.txt

COPY . /HateSpeechApp

ENTRYPOINT [ "python3" ]

CMD [ "webapp.py" ]