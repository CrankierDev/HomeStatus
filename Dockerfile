FROM python:3.10-alpine

RUN pip install --upgrade pip

WORKDIR /opt/HomeStatusDocker
COPY . /opt/HomeStatusDocker

RUN python -m venv /opt/HomeStatusDocker/venv
RUN source /opt/HomeStatusDocker/venv/bin/activate
RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1
EXPOSE 5000
CMD python homeStatus.py