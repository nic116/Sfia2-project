# FROM python:alpine3.11

# COPY . /opt/

# RUN apk update 

# # use apk for alpine and apt ... -y for ubuntu


# WORKDIR /opt/ 




# FROM python:3.7-alpine

# RUN apk add --update \
#   && pip3 install --upgrade pip

# WORKDIR /project/service_4/

# COPY ./requirements.txt .

# RUN pip3 install -r requirements.txt \
#   && rm -rf /var/cache/apk/*

# COPY . .

# CMD python3 app.py run -h 0.0.0.0



FROM python:latest

RUN mkdir service3
COPY . /service_3/
WORKDIR /service_3/
RUN apt-get update -y
RUN apt-get install python3-venv -y
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

ENTRYPOINT python3 app.py
