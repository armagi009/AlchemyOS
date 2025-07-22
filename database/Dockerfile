FROM postgres:15
RUN apt-get update && apt-get install -y postgresql-15-pgvector
COPY init.sql /docker-entrypoint-initdb.d/
