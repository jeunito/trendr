FROM python:2 
WORKDIR /opt/trendr/crawler

COPY . .

RUN mkdir -p /var/tmp/crawler
RUN python setup.py install
