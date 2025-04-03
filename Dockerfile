FROM python:3.12-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /myapp

COPY . /myapp
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]