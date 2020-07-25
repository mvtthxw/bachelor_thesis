#!/bin/bash

mkdir -p "/etc/port_scanner/ports" #przechowuje liste domyslnych portow i adres
mkdir -p "/tmp/port_scanner/tmp_scan" #przechwuje ostatni wynik scanu
mkdir -p "/tmp/port_scanner/tmp_result" #przechwuje ostatni oczyszczony wynik
mkdir -p "/var/log/port_scanner" #przechwuje raporty 

sudo apt-get update -y 
sudo apt-get install -y python3 docker docker.io

