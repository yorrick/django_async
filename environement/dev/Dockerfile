FROM python:2.7

ENV PYTHONUNBUFFERED 1

# libevent is already installed
RUN DEBIAN_FRONTEND=noninteractive apt-get install libevent-dev

# this dir
WORKDIR /app

#python manage.py syncdb --settings=django_async.settings_prod &&\
CMD pip install -r requirements-dev.txt &&\
    python manage.py runserver 0.0.0.0:8000 --settings=django_async.settings_dev
