FROM ubuntu:22.04

RUN	apt-get update && \ 
	apt-get install -y \
	ufw \
	rsyslog \
	python3-pip

RUN	pip3 install pika

COPY entrypoint.sh	/opt/scripts/entrypoint.sh
COPY ufw.conf		/etc/ufw/ufw.conf
COPY 49-ufw.conf	/etc/rsyslog.d/49-ufw.conf
COPY receive-action.py	/opt/scripts/receive-action.py

RUN chmod +x /opt/scripts/entrypoint.sh
RUN chmod +x /opt/scripts/receive-action.py

CMD ["sh", "-c", "/opt/scripts/entrypoint.sh && python3 /opt/scripts/receive-action.py"]
