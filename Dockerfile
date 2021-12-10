#!/bin/bash

FROM python:3.8
WORKDIR /app
COPY requirements-cpu.txt requirements-cpu.txt
RUN pip install -r requirements-cpu.txt
COPY . .
ENTRYPOINT ["python", "main.py"]
