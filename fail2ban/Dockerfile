FROM crazymax/fail2ban:latest

RUN apk update && \
	apk add python3 py3-pip && \
	python3 -m venv myenv
RUN /myenv/bin/pip install pika

CMD [ "fail2ban-server", "-f", "-x", "start" ]
