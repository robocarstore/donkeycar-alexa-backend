FROM python:3.7-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP app.py
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN pip3 install flask

RUN mkdir /app
WORKDIR /app

EXPOSE 80

CMD flask run --host=0.0.0.0 --port=80
