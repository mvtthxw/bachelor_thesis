FROM alpine:3.12


RUN apk update && apk add python3 nmap nmap-scripts
RUN apk update && apk add py-pip
RUN pip install python-nmap datetime
RUN mkdir /home/port_scanner

COPY main.py /home/port_scanner
COPY class_files /home/port_scanner/class_files
#COPY files /home/port_scanner/files

RUN touch /etc/periodic/min
RUN echo "*	*	*	*	*	run-parts /etc/periodic/min" >> /etc/crontabs/root

#CMD ['crond', '-b']