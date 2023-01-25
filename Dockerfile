FROM python:3.9 as python

RUN apt-get update && apt-get install -y \
  build-essential 

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt


WORKDIR /app

COPY ./src /app/

ENTRYPOINT ["python", "main.py"]
