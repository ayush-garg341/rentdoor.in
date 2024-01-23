FROM python:3.7-slim

# Add maintainer info
LABEL maintainer="Ayush Garg <gargayush341@gmail.com>"

RUN mkdir reviews
WORKDIR /reviews

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt && \
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y


# Copy the source code
COPY . .
