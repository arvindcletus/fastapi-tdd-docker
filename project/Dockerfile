# pull official base image
# Python version (use -bullseye variants on local arm64/Apple Silicon)
ARG VARIANT=3.10-bullseye
FROM python:${VARIANT}

# create the app user
RUN addgroup --system app && adduser --system --group app

# create the appropriate directories
ENV HOME=/usr/src
ENV APP_HOME=/usr/src/app

# set working directory
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

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

# chown all the files to the app user
RUN chown -R app:app $APP_HOME

# add entrypoint.sh
COPY ./entrypoint.sh .
RUN chmod + /usr/src/app/entrypoint.sh

# change to the app user
USER app

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
