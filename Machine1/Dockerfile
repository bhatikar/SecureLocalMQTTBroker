FROM ubuntu:18.04
RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y software-properties-common vim git python3-pip
RUN apt-get install -y build-essential mosquitto-clients  curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs
RUN pip3 install pip --upgrade
RUN pip3 install paho-mqtt python-dateutil flask flask_restful requests 
RUN apt-get install -y mosquitto vim iputils-ping net-tools
COPY test.js /
CMD node test.js
