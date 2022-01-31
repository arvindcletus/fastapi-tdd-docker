# pull official base image
# Python version (use -bullseye variants on local arm64/Apple Silicon)
ARG VARIANT=3.10-bullseye
FROM python:${VARIANT}

# set working directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# install python dependencies
COPY requirements.txt /tmp/pip-tmp/
RUN pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
  && rm -rf /tmp/pip-tmp

# add app
COPY . .

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod + /usr/src/app/entrypoint.sh

# Set up a non-root user
RUN groupadd -r user && useradd -r -g user user
USER user

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
