FROM python:3.10 AS python-build

RUN pip install --no-cache-dir mysqlclient

FROM python:3.10-slim

# Add maintainer info
LABEL maintainer="Ayush Garg <gargayush341@gmail.com>"

# Copy site packages from above python-build
COPY --from=python-build /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages

RUN mkdir reviews
WORKDIR /reviews

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt &&\
  apt-get update && \
  apt-get install -y --no-install-recommends gcc python3-dev libssl-dev libmariadb3 && \
  apt-get remove -y gcc python3-dev libssl-dev && \
  apt-get autoremove -y


# Copy the source code
COPY . .
EXPOSE 8000
