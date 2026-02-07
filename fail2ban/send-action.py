import argparse
import pika
import json
import logging
import sys

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--action')
parser.add_argument('-i', '--ip')


args = parser.parse_args()

ip = args.ip
action = args.action

message = {
    'ip': ip,
    'action': action
}

connection = pika.BlockingConnection(pika.ConnectionParameters(host='rabbit', port=5672))
channel = connection.channel()

channel.queue_declare(queue='fail2ban')

channel.basic_publish(exchange='',
                      routing_key='fail2ban',
                      body=json.dumps(message)
                      )
connection.close()

data = message
current_ip = data.get('ip')
current_action = data.get('action')

print(current_ip, 'showing current ip')
print(current_action, 'showing current action')
