FROM phpmyadmin/phpmyadmin:latest

RUN apt-get update
RUN apt-get install -y \
            iproute2

RUN mkdir /opt/data -p
COPY scripts/ /opt/scripts

WORKDIR /opt
ENTRYPOINT [ "scripts/entrypoint.sh" ]
CMD [ "apache2-foreground" ]