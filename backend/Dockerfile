FROM python:3.7

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend

COPY . .

RUN apt-get update

COPY requirements.txt .
RUN pip install -r requirements.txt