FROM python@sha256:73c7d5d218ff9e2d76f41edcc1bd4f71961f7551ea7b2e39ab8b4793cede21b4


# 一時ディレクトリを作成しない
ENV PYTHONDONTWRITEBYTECODE 1
# Djangoのログをターミナルに表示
ENV PYTHONUNBUFFERED 1

# 必要なライブラリーをインストール
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app