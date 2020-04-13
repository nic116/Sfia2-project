#FROM python:3.7-alpine
# FROM python:alpine3.11   


# RUN apk add --update \
#   && pip3 install --upgrade pip

# WORKDIR /project/service_2/

# COPY ./requirements.txt .

# RUN pip3 install -r requirements.txt \
#   && rm -rf /var/cache/apk/*

# COPY . .

# CMD python3 app.py run -h 0.0.0.0


FROM python:latest

RUN mkdir service2
COPY . /service_2/
WORKDIR /service_2/
RUN apt-get update -y
RUN apt-get install python3-venv -y
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install -r requirements.txt

ENTRYPOINT python3 app.py







# FROM python:3.7-alpine
# RUN apk add --update \
# && pip3 install --upgrade pip
# WORKDIR /project/Service_2/
# COPY /home/Admin/Dockerfile/requirements.txt .
# COPY . .
# EXPOSE 5000
# CMD python3 app.py run -h 0.0.0.0








# FROM python:alpine3.11   

# WORKDIR /opt/ 

# COPY . /opt/


# RUN apk update 




#ENTRYPOINT [ "" ]


# use apk for alpine and apt ... -y for ubuntu



#RUN printf "My Custom NGINX Image\n" > /usr/share/nginx/html/index.html

###  ^____ this is to follow courseware Dockerfiles


# use apk for alpine and apt ... -y for ubuntu
