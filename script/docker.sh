#!/bin/bash
# curl https://get.docker.com | sudo bash
echo "test1"
source ~/.bashrc
echo "test2"
sudo usermod -aG docker ${USER}
echo "test3"
sudo su - ${USER}
echo "test4"
docker stack deploy --compose-file docker-compose.yml  
echo "test5"


