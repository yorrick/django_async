FROM python:2.7

ENV PYTHONUNBUFFERED 1


RUN mkdir -p /usr/src/app
ADD . /usr/src/app

WORKDIR /usr/src/app

RUN rm -rf .git .gitignore .idea Dockerfile fig.yml

RUN pip install -r requirements-prod.txt

