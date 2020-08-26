FROM python:3
COPY requirements.txt /
WORKDIR /gridpoint_agent
COPY . .
RUN pip install -r /requirements.txt