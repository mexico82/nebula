FROM mysql

RUN apt-get update
RUN apt-get install -y \
            iproute2

RUN ln -s /var/lib/mysql /opt/data
COPY scripts/ /opt/scripts
COPY sql/ /docker-entrypoint-initdb.d

WORKDIR /opt
ENTRYPOINT [ "scripts/entrypoint.sh" ]
CMD [ "mysqld" ]