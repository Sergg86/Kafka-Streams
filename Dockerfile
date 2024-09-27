FROM python:bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG APP_DIR=/home/app/

COPY ./requirements.txt ${APP_DIR}

RUN set -ex && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r ${APP_DIR}requirements.txt

COPY . ${APP_DIR}

WORKDIR ${APP_DIR}

