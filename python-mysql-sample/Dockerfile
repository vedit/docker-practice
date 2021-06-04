FROM python:3.9.5-buster

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install -r requirements.txt

EXPOSE 3000

CMD [ "python","application.py"]
