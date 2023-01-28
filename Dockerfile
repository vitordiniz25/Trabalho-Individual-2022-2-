FROM python:3.8

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip
RUN pip install poetry
RUN poetry install