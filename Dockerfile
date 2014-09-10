FROM python:2.7

ENV PYTHONUNBUFFERED 1

# installs system packages
#RUN DEBIAN_FRONTEND=noninteractive apt-get install libevent-dev


RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app
RUN rm -rf .git .gitignore .idea Dockerfile fig.yml

RUN pip install -r requirements-prod.txt

