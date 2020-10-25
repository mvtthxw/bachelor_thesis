#!/bin/bash
sudo -s echo "25 6 * * * root docker run -it --rm  --name scanner -v $PWD/files:/home/port_scanner/files scanner:1" > /etc/crontab
