FROM ubuntu

RUN apt-get update && apt-get install -y mosquitto && apt-get install -y python3 && apt-get install -y python3-pip

ADD ./calc_serve.py /

RUN pip3 install paho-mqtt

EXPOSE 1883/tcp

CMD ["python3", "calc_serve.py"]
