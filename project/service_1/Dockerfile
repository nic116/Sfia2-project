# FROM python:3.7-alpine

# RUN apk add --update \
#   && pip3 install --upgrade pip

# WORKDIR /project/service_1/

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





# FROM python:alpine3.11   
# # nginx:latest 
# #FROM equivalent to pull

# COPY .  /opt/
# # copy  . /home/



# #RUN touch nic.txt /temp

# WORKDIR /opt/ 
# #change work directory so all the following commands will be as we were in the home directory

# #RUN chmod 775 scripts/*.sh

#ENTRYPOINT ["./venv/bin/python3","app.py"]
