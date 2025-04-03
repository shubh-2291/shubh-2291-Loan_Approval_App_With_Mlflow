FROM python:3.12-slim

# RUN apt update -y && apt install awscli -y
# Install system dependencies for mysqlclient
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config
    
WORKDIR /myapp

COPY . /myapp
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]