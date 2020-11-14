#!/bin/bash

sudo apt-get update
sudo apt-get install -y python3.6
sudo apt-get install -y docker
sudo apt-get install -y nmap

sudo apt-get install -y python3-pip

sudo pip3 install python-nmap
sudo python3 -m pip install python-nmap



#* * * * * root /home/mati/git/bachelor_thesis/test.sh - every minute
#0 10 * * * - daily at 10am