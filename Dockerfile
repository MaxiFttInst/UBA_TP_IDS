FROM debian:stable

WORKDIR /app

SHELL ["/bin/bash", "-c"]
RUN apt update && apt upgrade -y
RUN apt install pip python3 python3-flask python3-requests -y
