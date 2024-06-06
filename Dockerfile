FROM debian:stable

SHELL ["/bin/bash", "-c"]
RUN apt update && apt upgrade -y
RUN apt install pip python3 python3-venv -y
RUN python3 -m venv .venv
RUN . .venv/bin/activate && pip install mysql-connector-python Flask requests flask-sqlalchemy
