# Pull base image
FROM python:3.8
# Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1
# Set work directory
WORKDIR /djangocode

ADD . /djangocode

RUN pip install -r requirements.txt
# below CMD command will execute when Docker run command execute
CMD python manage.py runserver 0.0.0.0:8000