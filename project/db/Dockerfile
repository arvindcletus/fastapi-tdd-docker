# pull official base image
ARG VARIANT=14-alpine
FROM postgres:${VARIANT}

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
