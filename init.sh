#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3.6
sudo apt-get install -y docker
sudo apt-get install -y nmap

sudo apt-get install -y python3-pip

sudo pip3 install python-nmap
sudo python3 -m pip install python-nmap



#sudo bash -c 'cat << EOF > /etc/cron.daily/scanner
##!/bin/bash
#docker run -it --rm  --name scanner -v $PWD/files:/home/port_scanner/files scanner:1
#EOF'