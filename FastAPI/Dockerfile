# buster version for debian 10
FROM python:3.8-slim-buster

RUN mkdir app
WORKDIR /app

# install mssql driver
RUN apt-get update && apt-get install -y gcc curl gnupg unixodbc-dev
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt-get update && ACCEPT_EULA=Y apt-get -y install mssql-tools msodbcsql18
RUN echo 'export PATH="$PATH:/opt/mssql-tools/bin"' >> ~/.bashrc

# install python requirement module
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./.env /app
COPY ./run.py /app
COPY ./config/ /app/config/
COPY ./router/ /app/router/
COPY ./model/ /app/model/

