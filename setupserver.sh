#!/bin/sh

# Generate key value pair
ssh-keygen -o -t rsa -C "gargayush341@gmail.com"


# Clone the repo
git clone git@github.com:ayush-garg341/rentdoor.git
git reset --hard <commit_id>


# Install docker on ubuntu 20
sudo apt update
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt install docker-ce
sudo usermod -aG docker ${USER}

# Install docker-compose on ubuntu 20
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Run the application
sudo docker build -t rentdoor .
sudo docker-compose up -d

# Making the logs in /var/log directory
# But writing to this directory require permission, so to fix this
sudo chmod -R 777 /var/log
# TODO: Have to fix it permanent while booting up the application, set the permission to correct user which is running the application ...



