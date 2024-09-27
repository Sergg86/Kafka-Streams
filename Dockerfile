FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG APP_DIR=/home/app/

COPY ./requirements.txt ${APP_DIR}

RUN set -ex && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r ${APP_DIR}requirements.txt --no-deps

COPY . ${APP_DIR}

WORKDIR ${APP_DIR}

CMD ["sh", "-c", "python3 /home/app/main.py worker -l info"]
