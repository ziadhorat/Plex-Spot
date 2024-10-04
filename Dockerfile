FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk add --no-cache --virtual .build-deps gcc musl-dev \
    && pip install --no-cache-dir "setuptools>=70.0.0" \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps

COPY . .

ENV FLASK_APP=main.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8501

EXPOSE 8501

CMD ["flask", "run"]
