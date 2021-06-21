FROM python

ADD ./serv.py /

RUN pip install paho-mqtt
RUN pip install requests

EXPOSE 3300/tcp
EXPOSE 1882/tcp

CMD ["python", "serv.py"]
