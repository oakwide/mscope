FROM python:3.11-slim-bullseye

COPY . /opt/mscope
WORKDIR /opt/mscope

RUN python3 setup.py install

ENTRYPOINT ["mscope"]