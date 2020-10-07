FROM alpine:3.12


RUN apk update && apk add python3 nmap nmap-scripts
RUN apk update && apk add py-pip
RUN pip install python-nmap datetime
RUN mkdir /home/port_scanner
RUN mkdir -p /home/port_scanner/files


COPY main.py /home/port_scanner
COPY class_files /home/port_scanner/class_files

#ENV target=$target
RUN echo $target
WORKDIR /home/port_scanner
ENTRYPOINT python3 main.py $target
#RUN touch /etc/periodic/min
#RUN echo "*	*	*	*	*	run-parts /etc/periodic/min" >> /etc/crontabs/root

#CMD ['crond', '-b']
