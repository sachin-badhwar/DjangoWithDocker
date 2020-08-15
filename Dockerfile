# Pull base image
FROM python:3.8
# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /djangocode

ADD . /djangocode

COPY ./requirements.txt /djangocode/requirements.txt

RUN pip install -r requirements.txt

COPY . /djangocode

RUN pip install Pillow