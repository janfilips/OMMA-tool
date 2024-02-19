# Base image
FROM python:3.11.4-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.4.2

# Disable signature check
RUN echo 'Acquire::AllowInsecureRepositories "true";' > /etc/apt/apt.conf.d/allow-insecure
RUN echo 'APT::Get::AllowUnauthenticated "true";' >> /etc/apt/apt.conf.d/allow-insecure

# Install system dependencies
RUN apt-get update && apt-get install -y \
  postgresql-client \
  osm2pgsql \
  netcat-traditional \
  inetutils-ping \
  telnet \
  ntp \
  && rm -rf /var/lib/apt/lists/*

# Install NTP
RUN apt-get update && apt-get install -y ntp && rm -rf /var/lib/apt/lists/*
RUN ntpd -gq
ENV TZ=Europe/Vienna
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Install Poetry
RUN pip install "poetry==$POETRY_VERSION"

# Setup Timezone
RUN ln -sf /usr/share/zoneinfo/Europe/Burgas /etc/localtime && \
    echo "Europe/Vienna" > /etc/timezone

# Install psycopg2-binary directly
RUN pip install psycopg2-binary

# Copy the entire project directory
COPY . /code

# Copy only requirements to cache them in docker layer
WORKDIR /code
COPY poetry.lock pyproject.toml /code/

# Project initialization:
RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi
