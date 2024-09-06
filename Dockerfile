FROM python:3.11-slim

WORKDIR / config

COPY poetry.lock

RUN poetry install

COPY . .

CMD python manage.py runserver 0.0.0.0:8000