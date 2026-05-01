FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    curl \
    ansible \
    docker.io \
    docker-compose \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install requests==2.28.0

WORKDIR /app

COPY . /app/

CMD ["/bin/bash"]