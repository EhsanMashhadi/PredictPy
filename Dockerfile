#!/bin/bash

FROM python:3.8
WORKDIR /app
COPY requirements.txt requirements.txt
#RUN pip3 install pystan==2.19.1.1
#RUN pip3 install prophet
RUN pip install -r requirements.txt
COPY . .
#CMD [ "python3", "./main.py $FOO"]
ENTRYPOINT ["python", "main.py"]
