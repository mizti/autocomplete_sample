FROM python:2.7.13-alpine

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code

COPY ./src/* /code/
RUN set -ex \
    && apk add --no-cache --virtual build-dependencies \
       gcc \
       build-base \
       linux-headers \
    && pip install -r requirements.txt \
    && apk del build-dependencies

EXPOSE 8080
ENTRYPOINT ["/code/docker-entrypoint.sh"]
