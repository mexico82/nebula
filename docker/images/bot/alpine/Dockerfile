FROM python:alpine

RUN apk add --no-cache \
            build-base \
            libffi-dev \
            mariadb-connector-c-dev

VOLUME /root

RUN mkdir /opt/data -p
COPY scripts/ /opt/scripts

WORKDIR /opt
ENTRYPOINT [ "scripts/entrypoint.sh" ]
