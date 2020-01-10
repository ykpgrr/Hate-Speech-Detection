FROM ubuntu:16.04

LABEL maintainer="Yakup Görür <yakup.gorur@gmail.com>"

COPY . /app
WORKDIR /app

RUN apt-get update -y \
    && apt-get -y install python3 \
    && apt-get -y install python3-pip
RUN pip3 install -r requirements.txt


EXPOSE 5000
ENTRYPOINT [ "python3" ]

CMD [ "run_classifier_app.py" ]