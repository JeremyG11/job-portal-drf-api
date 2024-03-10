FROM python:3.10.6-slim-buster

WORKDIR /e-JobsAPI

COPY requirements.txt requirements.txt

RUN apt-get update

RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "manage.py", "runserver","0.0.0.0:8080", "--noreload"]